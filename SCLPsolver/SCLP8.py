import numpy as np
from subroutines.calc_boundaries import calc_boundaries
from subroutines.calc_init_basis import calc_init_basis
from subroutines.SCLP_solution8 import SCLP_solution
from subroutines.calc_controls5 import calc_controls
from subroutines.calc_objective import calc_objective
from subroutines.SCLP_solver8 import SCLP_solver
from subroutines.parametric_line8 import parametric_line

#function[t, x, q, u, p, firstbase, lastbase, pivots, Obj, Err, NN, stepcount, flopss, ecpu] = ...
#'#@profile
def SCLP(G, H, F, a, b, c, d, alpha, gamma, TT, settings, tolerance, tmp_path='', hot_start =False, save_solution = False):
#
#	[t,x,q,u,p,firstbase,lastbase,pivots,Obj,Err,NN,stepcount,flopss,ecpu] = ...
#		SCLP(G,H,F,a,b,c,d,alpha,gamma,TT,messagelevel,graphlevel,tol1,tol2,taxis,xaxis,qaxis)
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

    # STEPCOUNT = 0
    # DEPTH = 0
    # ITERATION = []
    K_DIM = G.shape[0]
    J_DIM = G.shape[1]
    I_DIM = H.shape[0]
    L_DIM = F.shape[1]

    if not hot_start:
        # Initiate top level problem, by obtaining the boundary and first dictionary
        x_0, q_N = calc_boundaries(G, F, H, b, d, alpha, gamma, tolerance)
        A, pn, dn, ps, ds, err = calc_init_basis(G, F, H, a, b, c, d, x_0, q_N, tolerance)
        if err['result'] != 0:
            raise Exception(err['message'])
        solution = SCLP_solution(pn, dn, A, K_DIM + L_DIM, J_DIM + I_DIM)
        klist = np.sort(np.append(pn[pn > 0], dn[dn > 0]))
        jlist = np.sort(-np.append(pn[pn < 0], dn[dn < 0]))
        # default constructor creates main parametric line
        param_line = parametric_line(np.vstack(x_0), np.vstack(q_N), klist, jlist, TT)
    else:
        import pickle
        print('Loading solution!')
        solution = pickle.load(open(tmp_path + 'solution.dat', 'rb'))
        param_line = pickle.load(open(tmp_path + 'param_line.dat','rb'))
        param_line.theta_bar = TT

    # Solve the problem, by a sequence of parametric steps

    solution, STEPCOUNT, pivot_problem = SCLP_solver(solution, param_line, 'toplevel',
                                           0, 0, dict(), settings, tolerance)

    # extract solution for output

    solution.update_state(param_line)
    u, p = calc_controls(solution, J_DIM + I_DIM, K_DIM + L_DIM)
    t = np.cumsum(np.hstack((0, solution.state.tau)))
    x = solution.state.x
    q = solution.state.q
    obj, err = calc_objective(alpha, a, b, gamma, c, d, u, x, p, q, solution.state.tau)
    if pivot_problem['result'] > 0 or save_solution:
        print('Saving solution!')
        solution.prepare_to_save()
        import pickle

        pickle.dump(solution, open(tmp_path + 'solution.dat', 'wb'))
        pickle.dump(param_line, open(tmp_path + 'param_line.dat', 'wb'))
    return t, x, q, u, p, solution.pivots, obj, err, solution.NN, STEPCOUNT