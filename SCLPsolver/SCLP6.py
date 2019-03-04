import numpy as np
import scipy.sparse as sp
from subroutines.calc_boundaries import calc_boundaries
from subroutines.calc_init_basis import calc_init_basis
from subroutines.extract_rates5 import extract_rates
from subroutines.SCLP_base_sequence import SCLP_base_sequence
from subroutines.SCLP_solution6 import SCLP_solution
from subroutines.calc_controls5 import calc_controls
from subroutines.calc_states4 import calc_states
from subroutines.calc_equations import calc_equations
from subroutines.calc_objective import calc_objective
from subroutines.SCLP_solver6 import SCLP_solver

#function[t, x, q, u, p, firstbase, lastbase, pivots, Obj, Err, NN, stepcount, flopss, ecpu] = ...
#'#@profile
def SCLP(G, H, F, a, b, c, d, alpha, gamma, TT, settings, tolerance):
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

    STEPCOUNT = 0
    DEPTH = 0
    ITERATION = []
    K_DIM = G.shape[0]
    J_DIM = G.shape[1]
    I_DIM = H.shape[0]
    L_DIM = F.shape[1]


    # Initiate top level problem, by obtaining the boundary and first dictionary
    x_0, q_N = calc_boundaries(G, F, H, b, d, alpha, gamma, tolerance)
    A, pn, dn, ps, ds, err = calc_init_basis(G, F, H, a, b, c, d, x_0, q_N, tolerance)
    if err['result'] != 0:
        raise Exception(err['message'])
    new_bs = SCLP_base_sequence({'prim_name': pn, 'dual_name': dn,'A': A})
    dx, dq = extract_rates(pn, dn, A, K_DIM + L_DIM, J_DIM + I_DIM)
    solution = SCLP_solution(None, new_bs, dx, dq)
    klist = np.sort(np.append(pn[pn > 0], dn[dn > 0]))
    jlist = np.sort(-np.append(pn[pn < 0], dn[dn < 0]))

    # Solve the problem, by a sequence of parametric steps
    #prim_name, dual_name, x_0, q_N, T, pivots, base_sequence = ...


    solution, x_0, q_N, T, STEPCOUNT, pivot_problem = SCLP_solver(solution, np.vstack(x_0), np.zeros((len(x_0),1)), np.vstack(q_N), np.zeros((len(q_N),1)), 0, 1, TT, 'toplevel',
                                           [], [], klist, jlist, K_DIM + L_DIM, J_DIM + I_DIM, 0, 0, dict(), settings, tolerance)

    # extract solution for output


    dx = solution.dx.get_matrix()
    dq = solution.dq.get_matrix()
    sdx = np.ones((dx.shape[0], dx.shape[1] + 2))
    sdq = np.ones((dq.shape[0], dq.shape[1] + 2))
    np.sign(dx, out = sdx[:, 1:-1])
    np.sign(dq, out = sdq[:, 1:-1])
    # check_sd(sdx, True)
    # check_sd(sdq, False)

    u, p = calc_controls(solution, J_DIM + I_DIM, K_DIM + L_DIM)

    tau, dtau = calc_equations(np.arange(1, K_DIM+L_DIM+1), np.arange(1,J_DIM+I_DIM+1), solution.pivots, x_0, np.zeros(len(x_0)), q_N, np.zeros(len(q_N)), T, 0, dx, dq)

    x, dum, q, dum = calc_states(dx, dq, x_0, np.zeros((len(x_0),1)), q_N, np.zeros((len(q_N),1)), tau, dtau, sdx, sdq, tolerance)

    NN = len(tau)
    t = np.cumsum(np.hstack((0, tau)))
    obj, err = calc_objective(alpha, a, b, gamma, c, d, u, x, p, q, tau)
    return t, x, q, u, p, solution.pivots, obj, err, NN, STEPCOUNT