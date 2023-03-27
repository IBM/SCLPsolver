# Copyright 2020 IBM Corporation
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import numpy as np
from .generic_SCLP_solution import generic_SCLP_solution
from .calc_objective import calc_objective
from .calc_controls import calc_controls
from .solution_state import solution_state
from .lp_tools.LP_formulation import solve_LP_in_place
from .parametric_line import parametric_line
import itertools


class SCLP_solution(generic_SCLP_solution):

    plot_width = 800
    plot_height = 400

    def __init__(self, formulation, x_0, q_N, tolerance, solver_settings):
        LP_form, ps, ds = formulation.formulate_ratesLP(x_0, q_N)
        LP_form, err = solve_LP_in_place(LP_form, ps, ds, tolerance)
        if err['result'] != 0:
            raise Exception(err['message'])
        super().__init__(LP_form, solver_settings, formulation.K + formulation.L, formulation.J + formulation.I)
        self._formulation = formulation
        self._final_T = 0
        self.last_T = 0
        self.max_valid_T = 0
        self._is_final = False
        self._u, self._p, self._t, self._obj, self._err= None, None, None, None, None
        if solver_settings.collect_plot_data:
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

    def update_state(self, param_line, check_state=False, tolerance=0, up_rewind=False):
        res = super().update_state(param_line, check_state, tolerance, up_rewind)
        if res and self.plot_data is not None:
            self.plot_data.append({'T': param_line.T, 'tau': self._state.tau, 'dtau': self._state.dtau})
        return res

    def get_final_solution(self, preserve = True):
        if not self._is_final:
            self._extract_final_solution(preserve)
        return self._t, self._state.x, self._state.q, self._u, self._p, self.pivots, self._obj, self._err, self.NN, self._state.tau, self.max_valid_T

    def _extract_final_solution(self, preserve = True):
        self._u, self._p = calc_controls(self, self._problem_dims.JJ, self._problem_dims.KK, preserve)
        self._t = np.cumsum(np.hstack((0, self._state.tau)))
        self._final_T = self._t[-1]
        self._obj, self._err = calc_objective(self._formulation, self._u, self._state.x, self._p, self._state.q, self._state.tau)
        self._is_final = True

    def check_final_solution(self, tolerance):
        is_ok = True
        if np.any(self._state.tau < -tolerance):
            n = np.argmin(self._state.tau)
            print('Negative tau!', n, self._state.tau[n])
            is_ok = False
        if np.any(self._state.x < -tolerance*10):
            n,i = np.unravel_index(np.argmin(self._state.x),self._state.x.shape)
            print('Negative primal state!',n,i, self._state.x[n,i])
            is_ok = False
        if np.any(self._state.q < -tolerance*10):
            print('Negative dual state!')
            is_ok = False
        return is_ok

    def is_other_feasible(self, other_sol, tolerance=1E-11):
        t,x,q,u,p,pivots,obj,err,NN,tau, maxT = other_sol.get_final_solution()
        # now we calculate important values at all points of the time partition, i.e. for t=t_0,...,t_N
        slack_u = np.vstack(self._formulation.b) - np.dot(self._formulation.H, u[:self._formulation.J, :]) # b - Hu(t)
        int_u = np.cumsum(u[:self._formulation.J,:]*tau, axis=1) # \int_0^t u(s) ds
        slack_dx = np.outer(self._formulation.a, np.cumsum(tau)) - np.dot(self._formulation.G, int_u) # at - G\int_0^t u(s) ds
        if self._formulation.L > 0:
            # this for the case when F \ne \emptyset (not our case)
            slack_x0 = np.vstack(self._formulation.alpha) - np.dot(self._formulation.F, x[self._formulation.K:, 0])
            real_dx = np.dot(self._formulation.F, np.cumsum(other_sol.state.dx[self._formulation.K:, :] * tau, axis=1))
            slack_dx = slack_dx - real_dx
        else:
            slack_x0 = np.vstack(self._formulation.alpha) # x^0 = \alpha (our case)
        slack_x = slack_dx + slack_x0 # x(t) = \alpha  + at - G\int_0^t u(s)  (our case)
        return np.all(slack_x >= -tolerance*10) and np.all(slack_u >= -tolerance*10) and np.all(slack_x0 >= -tolerance*10) # changed '>' to '>=' probably this was a problem

    def other_objective(self, other_sol):
        t,x,q,u,p,pivots,obj,err,NN,tau, maxT = other_sol.get_final_solution()
        TT = t[NN]
        part1 = np.dot(np.dot(self._formulation.gamma, u[:self._formulation.J, :]), tau)
        ddtau = tau * (t[:-1] + t[1:]) / 2
        part2 = np.dot(np.dot(self._formulation.c, u[:self._formulation.J, :]), tau * TT - ddtau)
        if self._formulation.L == 0:
            part3 = 0
        else:
            part3 = np.dot(np.dot(self._formulation.d, ((x[self._formulation.K:, :-1] + x[self._formulation.K:, 1:]) / 2)), tau)
        return part1 + part2 + part3

    def truncate_at(self, t0):
        self.t = np.cumsum(np.hstack((0, self._state.tau)))
        self._final_T = self.t[-1]
        if t0 < self._final_T:
            #TODO: check last_breakpoint
            last_breakpoint = np.where(self.t<=t0)[0][-1]
            delta_t = t0 - self.t[last_breakpoint]
            self._base_sequence.remove_bases(-1, last_breakpoint, self._pivots, self.bases_mm)
            self._pivots.remove_pivots(-1, last_breakpoint)
            self._state.tau=self._state.tau[last_breakpoint:]
            self._state.dtau = self._state.dtau[last_breakpoint:]
            self._state.del_x = self._state.del_x[:, last_breakpoint:]
            self._state.del_q = self._state.del_q[:, last_breakpoint:]
            self._state.x = self._state.x[:,last_breakpoint:]
            self._state.q = self._state.q[:, last_breakpoint:]
            self._dx.remove(0, last_breakpoint)
            self._dq.remove(0, last_breakpoint)
            self._state.dx = self._dx.get_matrix()
            self._state.dq = self._dq.get_matrix()
            self.loc_min_storage.update_caseI(-1, last_breakpoint, self._state.dx, self._state.dq)
            self._state.x[:, 0] += self._state.dx[:, 0] * delta_t
            self._state.x[self._state.dx[:, 0]==0, 0] = 0
            self._state.q[:, 0] += self._state.dq[:, 0] * delta_t


    def recalculate(self, param_line, t0, new_T, new_x0, settings, tolerance, mm = None):
        if t0 >= self._final_T:
            print('!!!')
        if new_T <= t0:
            print('!!!')
        self._is_final = False
        if new_x0 is not None:
            if new_T is None:
                new_T = param_line.T
            from .SCLP_x0_solver import SCLP_x0_solver
            STEPCOUNT, pivot_problem = SCLP_x0_solver(self, param_line, new_x0, new_T - t0, 0, 0, dict(),
                           settings, tolerance, settings.find_alt_line, mm)
            is_ok = self.update_state(param_line, check_state=settings.check_final_solution,
                                          tolerance=tolerance * 10)
            return STEPCOUNT, pivot_problem
        else:
            self.truncate_at(t0)
            if new_T is not None:
                from .SCLP_solver import SCLP_solver
                param_line  = parametric_line(np.ascontiguousarray(self._state.x[:, 0]), param_line.q_N, new_T-param_line.T, param_line.T-t0, del_T =1)
                param_line.build_boundary_sets(self.klist, self.jlist)
                self._state.reserve_memory_for_states()
                solution, STEPCOUNT, pivot_problem = SCLP_solver(self, param_line, 'update', 0, 0, dict(), settings, tolerance, settings.find_alt_line, mm)
                is_ok = solution.update_state(param_line, check_state=settings.check_final_solution,
                                              tolerance=tolerance * 10)
                return STEPCOUNT, pivot_problem
            else:
                return 0, {'result': 0}

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
            xstarts = [0]
            prev_tau = self.plot_data[0]['tau']
            yticks = []
            for r, dt_entry in enumerate(self.plot_data[1:]):
                y1 = last_T - prev_T
                y2 = last_T - dt_entry['T']
                ax1.plot([0, xstarts[-1]],[y1,y1], color='k')
                xends = np.cumsum(prev_tau + prev_tau * prev_dtau * (y1-y2))
                print(r)
                for i in range(len(xstarts)):
                    print(xstarts[i], y1, xends[i], y2)
                    ax1.plot([xstarts[i],xends[i]], [y1, y2], color='k')
                prev_T = dt_entry['T']
                xstarts = np.cumsum(dt_entry['tau'])
                prev_dtau = dt_entry['dtau']
                prev_tau = dt_entry['tau']
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

    def show_buffer_status(self):
        from bokeh.io import output_file, show
        from bokeh.plotting import figure
        from bokeh.palettes import Dark2_5 as line_palette
        # Plots of buffers status: piecewise linear graphs where:
        # t = [0,t1,...,Tres] vector containing time partition
        # X = (12,len(t)) matrix representing quantities at each of 12 buffers at each timepoint
        self.get_final_solution()

        number_of_buffers = self.formulation.K

        output_file("buffer_status.html")

        plot_line = figure(plot_width=self.plot_width, plot_height=self.plot_height)

        # create a color iterator
        colors = itertools.cycle(line_palette)

        # add a line renderer
        for i, color in zip(range(number_of_buffers), colors):
            plot_line.line(self.t, self._state.x[i], line_width=2, line_color=color)

        show(plot_line)
        return None

    def show_server_utilization(self):
        import pandas as pd
        from bokeh.core.property.dataspec import value
        from bokeh.io import output_file, show
        from bokeh.layouts import gridplot
        from bokeh.plotting import figure
        from bokeh.palettes import Category20
        # Plot of time_slots utilization:  4 barcharts where each bar can contain up to 12 colors. Colors are according to kind of tasks running on server
        #                                we have 12 kinds of tasks (number of columns in H) and 4 time_slots (number of rows in H)
        #                               if specific task (j) can run on the specific server (k) then we have H[k,j] > 0
        #                               otherwise H[k,j] == 0 and we cannot run specific task on specific server
        #                               U is a (16,len(t)-1) matrix where we interesting only on first (12,len(t)-1) part
        #                               U[j,n] * H[k,j] indicate how many capacity of server k took task j at time period t[n]...t[n+1]
        #                               we need for each server k create barchart where width of bar is length of time period
        #                               and total height is sum(U[n,j] * H[k,j]) for all j this height splitted by different colors according to j (up to 12)

        #self.extract_final_solution()

        number_of_buffers = self.formulation.K
        number_of_servers = self.formulation.I

        time_horizon = 150

        number_of_time_slots = len(self.t) - 1

        output_file('server_utilization.html')

        tasks = ['task ' + str(i) for i in range(1, len(self.formulation.H[0]) + 1)]
        new_legend_tasks = {}

        new_t = np.zeros(2 * number_of_time_slots)
        new_t[0] = self.t[1] / 2
        new_t[1:-1] = np.repeat(self.t[1:-1], 2)
        new_t[-1] = self.t[-1]

        data = {'t': new_t}

        new_matrix = np.zeros((number_of_buffers, 2 * number_of_time_slots))

        p = {}
        network_graph_tasks_indices = []
        network_graph_server_indices = []
        network_graph_tasks_server_hash = {}
        max_y_value = 1

        for k in range(number_of_servers):  # servers
            for j in range(number_of_buffers):  # tasks
                for ti in range(0, number_of_time_slots):  # time slices
                    new_matrix[j, 2 * ti] = self._u[j, ti] * self.formulation.H[k, j]
                    new_matrix[j, 2 * ti + 1] = self._u[j, ti] * self.formulation.H[k, j]
                if self.formulation.H[k, j] > 0:
                    new_legend_tasks[j] = 'task ' + str(j + 1)
                    network_graph_tasks_indices.append(j + 1)
                    network_graph_server_indices.append(len(tasks) + k + 1)
                    network_graph_tasks_server_hash[j + 1] = self.formulation.H[k, j]
                data['task ' + str(j + 1)] = new_matrix[j].tolist()

            df = pd.DataFrame(data)

            p[k] = figure(x_range=(0, time_horizon * 1.2), y_range=(0, max_y_value), plot_width=self.plot_width,
                          plot_height=self.plot_height, title='Server ' + str(k) + ' Utilization')

            p[k].varea_stack(stackers=tasks, x='t', color=Category20[number_of_buffers],
                             legend=[value(x) for x in tasks], source=df)

            # reverse the legend entries to match the stacked order
            for j in reversed(range(number_of_buffers)):
                if self.formulation.H[k, j] == 0:
                    del p[k].legend[0].items[j]

            p[k].legend[0].items.reverse()

        grid = gridplot([[p[0], p[1]], [p[2], p[3]]])
        show(grid)

        return None