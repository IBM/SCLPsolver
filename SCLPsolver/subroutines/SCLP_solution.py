import numpy as np
from .generic_SCLP_solution import generic_SCLP_solution
from .calc_init_basis import calc_init_basis
from .calc_objective import calc_objective
from .calc_controls import calc_controls
from .solution_state import solution_state


class SCLP_solution(generic_SCLP_solution):

    def __init__(self, formulation, x_0, q_N, tolerance, collect_plot_data):
        A, pn, dn, ps, ds, err = calc_init_basis(formulation, x_0, q_N, tolerance)
        if err['result'] != 0:
            raise Exception(err['message'])
        super().__init__(pn, dn, A, formulation.K + formulation.L, formulation.J + formulation.I)
        self._formulation = formulation
        self._final_T = 0
        if collect_plot_data:
            self.plot_data = []
        else:
            self.plot_data = None

    @property
    def formulation(self):
        return self._formulation

    def __getstate__(self):
        return self._problem_dims, self._pivots, self._base_sequence, self._dx, self._dq, self._last_collision, self._col_info_stack, self._klist, self._jlist, self._formulation

    def __setstate__(self, state):
        self._problem_dims, self._pivots, self._base_sequence, self._dx, self._dq, self._last_collision, self._col_info_stack, self._klist, self._jlist, self._formulation = state
        self.plot_data = None
        self.tmp_matrix = np.zeros_like(self._base_sequence.bases[0]['A'])
        self._state = solution_state()

    def update_state(self, param_line, check_state=False, tolerance=0):
        res = super().update_state(param_line, check_state, tolerance)
        if res and self.plot_data is not None:
            self.plot_data.append({'T': param_line.T, 'tau': self._state.tau, 'dtau': self._state.dtau})
        return res

    def extract_final_solution(self):
        u, p = calc_controls(self, self._problem_dims.JJ, self._problem_dims.KK)
        t = np.cumsum(np.hstack((0, self._state.tau)))
        self._final_T = t[-1]
        obj, err = calc_objective(self._formulation, u, self._state.x, p, self._state.q, self._state.tau)
        return t, self._state.x, self._state.q, u, p, self.pivots, obj, err, self.NN, self._state.tau

    def check_final_solution(self, tolerance):
        is_ok = True
        if np.any(self._state.tau < -tolerance):
            n = np.argmin(self._state.tau)
            print('Negative tau!', n, self._state.tau[n])
            is_ok = False
        if np.any(self._state.x < -tolerance):
            n,i = np.unravel_index(np.argmin(self._state.x),self._state.x.shape)
            print('Negative primal state!',n,i, self._state.x[n,i])
            is_ok = False
        if np.any(self._state.q < -tolerance):
            print('Negative dual state!')
            is_ok = False
        return is_ok

    def plot_history(self, plt):
        if self.plot_data is not None:
            if self._final_T == 0:
                last_T = sum(self._state.tau)
            else:
                last_T = self._final_T
            fig = plt.figure()
            ax1 = fig.add_subplot(111)
            ax1.plot([0,last_T], [last_T,0])
            prev_T = 0
            prev_dtau = self.plot_data[0]['dtau']
            xstarts = self.plot_data[0]['tau']
            yticks = []
            for dt_entry in self.plot_data[1:]:
                y1 = last_T - prev_T
                y2 = last_T - dt_entry['T']
                ax1.plot([0, xstarts[-1]],[y1,y1], color='k')
                xends = xstarts + prev_dtau * (dt_entry['T'] - prev_T)
                for i in range(len(xstarts)):
                    ax1.plot([xstarts[i],xends[i]], [y1, y2], color='k')
                prev_T = dt_entry['T']
                xstarts = np.cumsum(dt_entry['tau'])
                prev_dtau = np.cumsum(dt_entry['dtau'])
                yticks.append(y1)
            # set the x-spine (see below for more info on `set_position`)
            ax1.spines['left'].set_position('zero')
            # turn off the right spine/ticks
            ax1.spines['right'].set_color('none')
            ax1.yaxis.tick_left()
            # set the y-spine
            ax1.spines['bottom'].set_position('zero')
            # turn off the top spine/ticks
            ax1.spines['top'].set_color('none')
            ax1.xaxis.tick_bottom()
            ax1.set_xticks(xends)
            ax1.set_yticks(yticks)
            ax1.set_yticklabels(list(range(len(self.plot_data))))
            plt.setp(ax1.get_xticklabels(), rotation=30)
            return plt
        return None

