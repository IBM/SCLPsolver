import numpy as np
from bokeh.core.property.dataspec import value
from bokeh.io import output_file, show
from bokeh.layouts import gridplot
from bokeh.plotting import figure
from bokeh.palettes import Dark2_5 as line_palette
from bokeh.palettes import Category20 as stacked_bar_chart_palette
from bokeh.palettes import Category20, Paired, Plasma256
import pandas as pd
from doe.data_generators.MCQN import generate_MCQN_data
from .generic_SCLP_solution import generic_SCLP_solution
from .calc_objective import calc_objective
from .calc_controls import calc_controls
from .solution_state import solution_state
from .LP_formulation import solve_LP_in_place
import itertools


class SCLP_solution(generic_SCLP_solution):

    plot_width = 800
    plot_height = 400

    def __init__(self, formulation, x_0, q_N, tolerance, collect_plot_data):
        LP_form = formulation.formulate_ratesLP(x_0, q_N)
        err = solve_LP_in_place(LP_form, np.zeros_like(LP_form.simplex_dict), tolerance)
        if err['result'] != 0:
            raise Exception(err['message'])
        super().__init__(LP_form, formulation.K + formulation.L, formulation.J + formulation.I)
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

    def show_buffer_status(self):
        # Plots of buffers status: piecewise linear graphs where:
        # t = [0,t1,...,Tres] vector containing time partition
        # X = (12,len(t)) matrix representing quantities at each of 12 buffers at each timepoint
        t, X, q, U, p, pivots, obj, err, NN, tau = self.extract_final_solution()

        number_of_buffers = len(X)

        output_file("buffer_status.html")

        plot_line = figure(plot_width=self.plot_width, plot_height=self.plot_height)

        # create a color iterator
        colors = itertools.cycle(line_palette)

        # add a line renderer
        for i, color in zip(range(number_of_buffers), colors):
            plot_line.line(t, X[i], line_width=2, line_color=color)

        show(plot_line)
        return None

    def show_server_utilization(self):
        # Plot of time_slots utilization:  4 barcharts where each bar can contain up to 12 colors. Colors are according to kind of tasks running on server
        #                                we have 12 kinds of tasks (number of columns in H) and 4 time_slots (number of rows in H)
        #                               if specific task (j) can run on the specific server (k) then we have H[k,j] > 0
        #                               otherwise H[k,j] == 0 and we cannot run specific task on specific server
        #                               U is a (16,len(t)-1) matrix where we interesting only on first (12,len(t)-1) part
        #                               U[j,n] * H[k,j] indicate how many capacity of server k took task j at time period t[n]...t[n+1]
        #                               we need for each server k create barchart where width of bar is length of time period
        #                               and total height is sum(U[n,j] * H[k,j]) for all j this height splitted by different colors according to j (up to 12)

        t, X, q, U, p, pivots, obj, err, NN, tau = self.extract_final_solution()

        number_of_buffers = len(X)
        number_of_servers = 4
        seed = 1000

        time_horizon = 150

        G, H, F, gamma, c, d, alpha, a, b, TT, buffer_cost = generate_MCQN_data(seed, number_of_buffers,
                                                                                number_of_servers)

        number_of_time_slots = len(t) - 1

        output_file('server_utilization.html')
        # create a color iterator
        colors = stacked_bar_chart_palette[len(H[0])]

        time_slots = ['t ' + str(i) for i in range(number_of_time_slots)]

        tasks = ['task ' + str(i) for i in range(1, len(H[0]) + 1)]
        new_legend_tasks = {}

        new_t = np.zeros(2 * number_of_time_slots)
        new_t[0] = t[1] / 2
        new_t[1:-1] = np.repeat(t[1:-1], 2)
        new_t[-1] = t[-1]

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
                    new_matrix[j, 2 * ti] = U[j, ti] * H[k, j]
                    new_matrix[j, 2 * ti + 1] = U[j, ti] * H[k, j]
                if H[k, j] > 0:
                    new_legend_tasks[j] = 'task ' + str(j + 1)
                    network_graph_tasks_indices.append(j + 1)
                    network_graph_server_indices.append(len(tasks) + k + 1)
                    network_graph_tasks_server_hash[j + 1] = H[k, j]
                data['task ' + str(j + 1)] = new_matrix[j].tolist()

            df = pd.DataFrame(data)

            p[k] = figure(x_range=(0, time_horizon * 1.2), y_range=(0, max_y_value), plot_width=self.plot_width,
                          plot_height=self.plot_height, title='Server ' + str(k) + ' Utilization')

            p[k].varea_stack(stackers=tasks, x='t', color=Category20[number_of_buffers],
                             legend=[value(x) for x in tasks], source=df)

            # reverse the legend entries to match the stacked order
            for j in reversed(range(number_of_buffers)):
                if H[k, j] == 0:
                    del p[k].legend[0].items[j]

            p[k].legend[0].items.reverse()

        grid = gridplot([[p[0], p[1]], [p[2], p[3]]])
        show(grid)

        return None