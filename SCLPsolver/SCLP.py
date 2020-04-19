import os
from subroutines.SCLP_solution import SCLP_solution
from subroutines.SCLP_formulation import SCLP_formulation
from subroutines.SCLP_solver import SCLP_solver
from subroutines.utils import relative_to_project

class SCLP_settings():

    def __init__(self, find_alt_line =True, tmp_path=None, file_name = None, memory_management= True, hot_start =False,
                 save_solution = False, check_final_solution=True, check_intermediate_solution=False, suppress_printing = False,
                 rewind_max_delta = 10E-2, collect_plot_data=False, max_iteration = None):
        self.find_alt_line = find_alt_line
        self.hot_start = hot_start
        self.file_name = file_name
        self.save_solution = save_solution
        self.check_final_solution = check_final_solution
        self.check_intermediate_solution = check_intermediate_solution
        self.memory_management = memory_management
        self.max_iteration = max_iteration
        self.suppress_printing = suppress_printing
        self.rewind_max_delta = rewind_max_delta
        self.collect_plot_data = collect_plot_data
        if tmp_path is None:
            self.tmp_path = relative_to_project('')
        elif os.path.isdir(tmp_path):
            self.tmp_path = tmp_path
        else:
            self.tmp_path = relative_to_project('')

#'#@profile
def SCLP(G, H, F, a, b, c, d, alpha, gamma, TT, settings = SCLP_settings(), tolerance=1E-11):
#
#	solves the separated continuous linear program:
#
#	Find  x,uSCLP1
#			max 	int_0^T  (gamma + (T-t) c) u(t) + d x(t) dt
#
#			s.t.	int_0^t G u(s) ds + F x(t) ? alpha + a t
#							H u(t)			   ?  b
#							u,x ? 0,  0 < t < T.
#
#	and the dual separated continuous linear program:
#
#	Find  q,p
#			min 	int_0^T  (alpha + (T-t) a)' p(t) + b' q(t) dt
#
#			s.t.	int_0^t G' p(s) ds + H' q(t) ? gamma' + c' t
#							F' p(t)			     ?  d'
#							p,q ? 0,  0 < t < T.
#
#
#	Input parameters:	G 		is KxJ array
#						H 		is IxJ array
#						F       is KxL array
#						alpha,a		are K column vectors
#						b			is I column vector
#						gamma,c		is J row vector
#						d			is L row vector
#						TT			scalar, time horizon
#								if TT = Inf  problem is solved for all ranges of T
#
#						MESSAGELEVEL = messagelevel
#						GRAPHLEVEL = graphlevel
#
#						TOL1 = tol1		numerical precision value rounde to zero
#						TOL2 = tol2		numerical precision value for comparisons
#
#						taxis,xaxis,qaxis	axes lengths for plots (Inf allowed)
#
#
#	Output parameters:	t		vector of the N+1 breakpoints
#						x		(K+L)x(N+1) array
#						q		(J+I)x(N+1) array
#						u		(J+I)xN	array
#						p		(K+L)xN	array
#						firstbase	The first basis in the solution base sequence
#						lastbase 	The first basis in the solution base sequence
#						pivots		The sequence of pivots in the solution base sequence
#						Obj		scalar, objective value
#						Err		scalar, objective error |primal-dual|
#						inters  counts the number of intervals in the final solution
#						pivots	counts the number of pivots
#						flopss	counts the number of floating point operations
#						ecpu	elapsed CPU time
#
#	To create movie re-run with values of:
#
#						taxis	time range
#						xaxis	x range
#						qaxis	q range
#

    formulation = SCLP_formulation(G, F, H, a, b, c, d, alpha, gamma, TT)
    if not settings.hot_start:
        # Initiate top level problem, by obtaining the boundary and first dictionary
        # default constructor creates main parametric line
        param_line = formulation.get_parametric_line(tolerance)
        # calculate initial basis
        solution = SCLP_solution(formulation, param_line.x_0, param_line.q_N, tolerance, settings)
        # building Kset0 and JsetN
        param_line.build_boundary_sets(solution.klist, solution.jlist)
    else:
        import pickle
        print('Loading solution!')
        if settings.file_name is not None:
            solution_file_name = settings.tmp_path + '/' + settings.file_name + '_solution.dat'
            line_file_name = settings.tmp_path + '/' + settings.file_name + '_param_line.dat'
        else:
            solution_file_name = settings.tmp_path + '/solution.dat'
            line_file_name = settings.tmp_path + '/param_line.dat'
        try:
            solution = pickle.load(open(solution_file_name, 'rb'))
            param_line = pickle.load(open(line_file_name,'rb'))
        except IOError:
            raise Exception('Solution files not found in: ' + settings.tmp_path)
        param_line.theta_bar = TT

    if settings.memory_management:
        from subroutines.memory_manager import memory_manager
        mm = memory_manager(formulation.K, formulation.J + formulation.L, formulation.I)
    else:
        mm = None

    # Solve the problem, by a sequence of parametric steps
    solution, STEPCOUNT, pivot_problem = SCLP_solver(solution, param_line, 'toplevel',
                                           0, 0, dict(), settings, tolerance, settings.find_alt_line, mm)

    # extract solution for output
    is_ok = solution.update_state(param_line, check_state=settings.check_final_solution, tolerance = tolerance *10)
    if pivot_problem['result'] > 0 or settings.save_solution or not is_ok:
        print('Saving solution!')
        solution.prepare_to_save()
        import pickle
        if settings.file_name is None:
            file_name = 'SCLP'
        else:
            file_name = settings.file_name
        solution_file_name = settings.tmp_path + '/' + file_name + '_' + str(STEPCOUNT) +'_solution.dat'
        line_file_name = settings.tmp_path + '/' + file_name + '_' + str(STEPCOUNT) + '_param_line.dat'
        pickle.dump(solution, open(solution_file_name, 'wb'))
        pickle.dump(param_line, open(line_file_name, 'wb'))
    return solution, STEPCOUNT, param_line.T, pivot_problem['result']