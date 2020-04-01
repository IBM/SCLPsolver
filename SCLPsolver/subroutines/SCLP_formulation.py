import numpy as np
from enum import Enum
from .matlab_utils import find, ismember
from .lp_tools.LP_formulation import LP_formulation
from .lp_tools.simplex_procedures import unsigned_simplex
from .piecewise_data import piecewise_data
from .parametric_line import parametric_line


class SCLP_formulation_type(Enum):
    primal_classic = 0
    dual_classic = 1
    weiss = 2
    not_bounded = 3
    primal_MCLP = 4
    dual_MCLP = 5
    both_MCLP = 6
    primal_infeasible = 7
    dual_infeasible = 8
    both_infeasible = 9

class SCLP_data_type(Enum):
    linear = 0
    primal_piecewise_linear = 1
    dual_piecewise_linear = 2
    piecewise_linear = 3


# We are going to extend this class
# Assume that a,b,c,d are matrix
class SCLP_formulation():

    __slots__ = ["G", "F", "H", "a", "b", "c", "d", "alpha", "gamma", "T", "I", "J", "K", "L", "_formulation_type", "_data_type"]

    def __init__(self, G, F, H, a, b, c, d, alpha, gamma, T):
        self.G, self.F, self.H, self.a, self.b, self.c, self.d, self.alpha, self.gamma, self.T = G, F, H, a, b, c, d, alpha, gamma, T
        self.K = G.shape[0]
        self.J = G.shape[1]
        self.I = H.shape[0]
        self.L = F.shape[1]
        if self.L == 0:
            if self.I == 0:
                if np.any(self.alpha < 0):
                    if np.any(self.gamma > 0):
                        self._formulation_type = SCLP_formulation_type.both_MCLP
                    else:
                        self._formulation_type = SCLP_formulation_type.primal_MCLP
                else:
                    if np.any(self.gamma > 0):
                        self._formulation_type = SCLP_formulation_type.dual_MCLP
                    else:
                        self._formulation_type = SCLP_formulation_type.not_bounded
            else:
                self._formulation_type = SCLP_formulation_type.primal_classic
                if np.any(self.alpha < 0):
                    self._formulation_type = SCLP_formulation_type.primal_MCLP
        else:
            if self.I == 0:
                self._formulation_type = SCLP_formulation_type.dual_classic
                if np.any(self.gamma > 0):
                    self._formulation_type = SCLP_formulation_type.dual_MCLP
            else:
                self._formulation_type = SCLP_formulation_type.weiss
        if isinstance(a, piecewise_data):
            if isinstance(c, piecewise_data):
                self._data_type = SCLP_data_type.piecewise_linear
            else:
                self._data_type = SCLP_data_type.primal_piecewise_linear
        else:
            if isinstance(c, piecewise_data):
                self._data_type = SCLP_data_type.dual_piecewise_linear
            else:
                self._data_type = SCLP_data_type.linear

    @property
    def data_type(self):
        return self._data_type

    @property
    def formulation_type(self):
        return self._formulation_type

    def formulate_ratesLP(self, x_0, q_N):
        Kset = find(x_0)
        Jset = find(q_N)
        DD = np.vstack((-np.hstack((0, self.c, self.d)), np.hstack((np.vstack(self.a), self.G, self.F)),
                          np.hstack((np.vstack(self.b), self.H, np.zeros((self.I, self.L))))))
        DD = np.ascontiguousarray(DD)
        pn = np.hstack((np.arange(1, self.K + 1), -np.arange(self.J + 1, self.J + self.I + 1)), dtype = int)
        psx = ismember(np.arange(0, self.K), Kset).astype(int)
        psu = -ismember(np.arange(self.J, self.J + self.I), Jset).astype(int)
        ps = np.hstack((psx, psu))

        dn = np.hstack((-np.arange(1, self.J + 1), np.arange(self.K + 1, self.K + self.L + 1)), dtype = int)
        dsq = ismember(np.arange(0, self.J), Jset).astype(int)
        dsp = -ismember(np.arange(self.K, self.K + self.L), Kset).astype(int)
        ds = np.hstack((dsq, dsp))
        return LP_formulation(DD, pn, dn), ps, ds

    def get_primalBoundaryLP(self):
        DD1 = np.vstack((-np.hstack((0, self.d)), np.hstack((np.vstack(self.alpha), self.F))))
        pn1 = np.arange(1, self.K + 1, dtype = int)
        dn1 = np.arange(self.K + 1, self.K + self.L + 1, dtype = int)
        return LP_formulation(DD1, pn1, dn1)

    def get_dualBoundaryLP(self):
        DD1 = np.vstack((np.hstack((0, np.hstack(self.b))), np.hstack((np.vstack(-self.gamma), -self.H.transpose()))))
        pn1 = np.arange(1, self.J + 1, dtype = int)
        dn1 = np.arange(self.J + 1, self.J + self.I + 1, dtype = int)
        return LP_formulation(DD1, pn1, dn1)

    def get_generalBoundaryLP(self):
        DD0 = np.vstack((np.hstack((0, -self.gamma, np.zeros((1, self.L)), self.d)), np.hstack((self.alpha, self.G, self.F)),
                         np.hstack((np.zeros((self.I, 1)), self.H, np.zeros((self.I, self.L))))))
        pn = np.concatenate((np.arange(1, self.K + 1), -np.arange(self.J + 1, self.J + self.I + 1)), dtype = int)
        dn = np.concatenate((-np.arange(1, self.J + 1), np.arange(self.K + 1, self.K + self.L + 1)), dtype = int)
        return LP_formulation(DD0, pn, dn)

    def get_general_dualBoundaryLP(self):
        DD0 = np.vstack(
            (np.hstack((0, -self.gamma, np.zeros((1, self.L)), self.d)), np.hstack((self.alpha, self.G, self.F)),
             np.hstack((np.zeros((self.I, 1)), self.H, np.zeros((self.I, self.L))))))
        pn = np.concatenate((np.arange(1, self.K + 1), -np.arange(self.J + 1, self.J + self.I + 1)))
        dn = np.concatenate((-np.arange(1, self.J + 1), np.arange(self.K + 1, self.K + self.L + 1)))
        return LP_formulation(DD0, pn, dn)

    def get_dualBoundaryLP_solution(self, tolerance = 0):
        if self._formulation_type == SCLP_formulation_type.not_bounded or self._formulation_type == SCLP_formulation_type.dual_classic:
            return -self.gamma
        elif self._formulation_type == SCLP_formulation_type.primal_classic or self._formulation_type == SCLP_formulation_type.weiss:
            LP_form = self.get_dualBoundaryLP()
            LP_form, err = unsigned_simplex(LP_form, None, tolerance)
            if err['result'] == 0:
                q_N = np.zeros(self.J + self.I)
                q_N[LP_form.prim_name - 1] = LP_form.simplex_dict[1:, 0]
                return q_N
        LP_form = self.get_generalBoundaryLP()
        LP_form, err = unsigned_simplex(LP_form, None, tolerance)
        if err['result'] == 0:
            q_N = np.zeros(self.J + self.I)
            q_N[LP_form.prim_name - 1] = LP_form.simplex_dict[1:, 0]
            return q_N
        return None

    def get_primalBoundaryLP_solution(self, tolerance = 0):
        if self._formulation_type == SCLP_formulation_type.not_bounded or self._formulation_type == SCLP_formulation_type.primal_classic:
            return self.alpha
        elif self._formulation_type == SCLP_formulation_type.dual_classic or self._formulation_type == SCLP_formulation_type.weiss:
            LP_form = self.get_primalBoundaryLP()
            LP_form, err = unsigned_simplex(LP_form, None, tolerance)
            if err['result'] == 0:
                x_0 = np.zeros(self.K + self.L)
                x_0[LP_form.prim_name - 1] = LP_form.simplex_dict[1:, 0]
                return x_0
        # MCLP not supported yet
        return None

    def get_parametric_line(self, tolerance = 0):
        x_0 = self.get_primalBoundaryLP_solution(tolerance)
        q_N = self.get_dualBoundaryLP_solution(tolerance)
        return parametric_line(x_0, q_N, self.T)

    def show_task_capacity_per_server(self):
        from bokeh.io import output_file, show
        from bokeh.models import GraphRenderer, Oval, StaticLayoutProvider, ColumnDataSource, LabelSet
        from bokeh.plotting import figure
        from bokeh.palettes import Category20c, Category20
        # we have 12 kinds of tasks (number of columns in H) and 4 time_slots (number of rows in H)
        number_of_servers = len(self.H)
        tasks = ['task ' + str(i) for i in range(1, len(self.H[0]) + 1)]

        index_array_of_tasks = list(range(1, len(tasks) + 1))
        index_array_of_servers = list(range(len(tasks) + 1, len(tasks) + number_of_servers + 1))

        number_of_tasks = len(tasks)

        node_indices = np.concatenate((index_array_of_tasks, index_array_of_servers), axis=None).tolist()
        node_x_location = np.concatenate((index_array_of_tasks, list(range(1, len(index_array_of_servers) + 1))),
                                         axis=None).tolist()
        node_y_location = np.concatenate(
            (np.full(len(index_array_of_tasks), 5), np.full(len(index_array_of_servers), 3)), axis=None).tolist()

        plot = figure(title='Task capacity per server', x_range=(0, max(number_of_servers, number_of_tasks) + 1),
                      y_range=(0, 8),
                      tools='', toolbar_location=None)

        graph = GraphRenderer()

        graph.node_renderer.data_source.add(node_indices, 'index')
        graph.node_renderer.data_source.add(Category20c[len(node_indices)], 'color')
        graph.node_renderer.glyph = Oval(height=0, width=0, fill_color='color')

        network_graph_tasks_indices = []
        network_graph_server_indices = []
        network_graph_tasks_server_hash = {}

        for k in range(number_of_servers):  # servers
            for j in range(number_of_tasks):  # tasks
                if self.H[k, j] > 0:
                    network_graph_tasks_indices.append(j + 1)
                    network_graph_server_indices.append(len(tasks) + k + 1)
                    network_graph_tasks_server_hash[j + 1] = self.H[k, j]

        graph.edge_renderer.data_source.data = dict(
            start=list(network_graph_tasks_indices),
            end=list(network_graph_server_indices)
        )

        x = node_x_location
        y = node_y_location

        graph_layout = dict(zip(node_indices, zip(x, y)))
        graph.layout_provider = StaticLayoutProvider(graph_layout=graph_layout)

        plot.renderers.append(graph)

        x_servers = list(range(1, len(index_array_of_servers) + 1))
        y_servers = np.full(len(index_array_of_servers), 3)
        plot.square(x_servers, y_servers, size=30, color=Category20[number_of_servers], alpha=0.5)

        x_tasks = index_array_of_tasks
        y_tasks = np.full(len(index_array_of_tasks), 5)
        plot.circle(x_tasks, y_tasks, size=30, color=Category20[len(index_array_of_tasks)], alpha=0.5)
        text_label_values = np.round(
            np.multiply(np.round(list(network_graph_tasks_server_hash.values()), 2), 100)).tolist()
        text_label_values = [str(int(capacity)) + '%' for capacity in text_label_values]

        source = ColumnDataSource(data=dict(x=list(network_graph_tasks_server_hash.keys()),
                                            y=np.full(len(network_graph_tasks_indices), 4.8),
                                            values=text_label_values))
        capacityLabels = LabelSet(x='x', y='y', text='values', level='glyph',
                                  x_offset=-8, y_offset=10, source=source, render_mode='canvas', text_font_size="10pt")

        plot.add_layout(capacityLabels)

        source = ColumnDataSource(data=dict(x=[6, 6],
                                            y=[2.5, 5.5],
                                            values=['servers', 'tasks']))

        typeLabel = LabelSet(x='x', y='y', text='values', level='glyph',
                             x_offset=0, y_offset=0, source=source, render_mode='canvas', text_font_size="10pt")
        plot.add_layout(typeLabel)

        output_file('graph.html')
        show(plot)

        return None

    def show_flow_from_outside_to_buffers_to_tasks(self):
        from bokeh.io import output_file, show
        from bokeh.models import GraphRenderer, Oval, StaticLayoutProvider, ColumnDataSource, LabelSet, Arrow, OpenHead
        from bokeh.plotting import figure
        from bokeh.palettes import Plasma256
        # vector alpha >0 , vector a can be any value
        # a is input/output coming from outside
        # alpha is initial value in buffer
        # matrix G connected buffers and tasks
        # in matrix G , flow between a task and multiple buffers
        # a to buffer to task

        number_of_io_nodes = len(self.a)
        number_of_buffers = self.K
        number_of_tasks = len(self.H[0])
        index_array_of_io = list(range(1, number_of_io_nodes + 1))
        index_array_of_buffers = list(range(number_of_io_nodes + 1, number_of_io_nodes + number_of_buffers + 1))
        index_array_of_tasks = list(range(number_of_io_nodes + number_of_buffers + 1,
                                          number_of_io_nodes + number_of_buffers + number_of_tasks + 1))

        node_indices = np.concatenate((index_array_of_io, index_array_of_buffers, index_array_of_tasks),
                                      axis=None).tolist()
        node_x_location = np.concatenate((index_array_of_io, list(range(1, len(index_array_of_buffers) + 1)),
                                          list(range(1, len(index_array_of_tasks) + 1))), axis=None).tolist()
        node_y_location = np.concatenate(
            (np.full(number_of_io_nodes, 7), np.full(number_of_buffers, 5), np.full(number_of_tasks, 3)),
            axis=None).tolist()

        max_x_range = max(number_of_io_nodes, number_of_buffers, number_of_tasks) + 1

        plot = figure(title='Flow from outside to buffers to tasks', x_range=(0, max_x_range), y_range=(0, 9),
                      tools='', toolbar_location=None)

        graph = GraphRenderer()

        graph.node_renderer.data_source.add(node_indices, 'index')
        graph.node_renderer.data_source.add(Plasma256[:len(node_indices)], 'color')
        graph.node_renderer.glyph = Oval(height=0, width=0, fill_color='color')

        start = index_array_of_io
        end = index_array_of_buffers

        network_graph_buffer_task_hash = {}

        for buffer_index in range(number_of_buffers):
            network_graph_buffer_task_hash[buffer_index + 1] = np.sum(self.G[buffer_index, :])

        graph.edge_renderer.data_source.data = dict(
            start=start,
            end=end
        )

        x = node_x_location
        y = node_y_location

        graph_layout = dict(zip(node_indices, zip(x, y)))
        graph.layout_provider = StaticLayoutProvider(graph_layout=graph_layout)

        plot.renderers.append(graph)

        x_io = list(range(1, number_of_io_nodes + 1))
        y_io = np.full(number_of_io_nodes, 7)
        plot.triangle(x_io, y_io, size=30, color=getLargePalette(number_of_io_nodes,Plasma256), alpha=0.5, line_width=2)

        x_buffers = list(range(1, number_of_buffers + 1))
        y_buffers = np.full(number_of_buffers, 5)
        plot.rect(x_buffers, y_buffers, color=getLargePalette(number_of_buffers,Plasma256), alpha=0.5, width=0.5, height=0.5)

        x_tasks = list(range(1, number_of_tasks + 1))
        y_tasks = np.full(number_of_tasks, 3)
        plot.circle(x_tasks, y_tasks, size=30, color=getLargePalette(number_of_tasks,Plasma256), alpha=0.5)

        for i in range(number_of_buffers):
            for j in range(number_of_tasks):
                if self.G[i, j] > 0:
                    x_start_node = x_buffers[i]
                    y_start_node = y_buffers[i]
                    x_end_node = x_tasks[j]
                    y_end_node = y_tasks[j]
                elif self.G[i, j] < 0:
                    x_start_node = x_tasks[j]
                    y_start_node = y_tasks[j]
                    x_end_node = x_buffers[i]
                    y_end_node = y_buffers[i]
                plot.add_layout(Arrow(end=OpenHead(),
                                      x_start=x_start_node, y_start=y_start_node, x_end=x_end_node, y_end=y_end_node))

        text_label_values = np.round(
            np.multiply(np.round(list(network_graph_buffer_task_hash.values()), 2), 100)).tolist()
        text_label_values = [str(int(capacity)) + '%' for capacity in text_label_values]

        source = ColumnDataSource(data=dict(x=list(network_graph_buffer_task_hash.keys()),
                                            y=np.full(number_of_buffers, 4.8),
                                            values=text_label_values))
        capacityLabels = LabelSet(x='x', y='y', text='values', level='glyph',
                                  x_offset=-8, y_offset=10, source=source, render_mode='canvas', text_font_size="10pt")

        plot.add_layout(capacityLabels)

        source = ColumnDataSource(data=dict(x=[max_x_range / 2 - 0.5, max_x_range / 2 - 0.5, max_x_range / 2 - 0.5],
                                            y=[2.5, 5.5, 7.5],
                                            values=['tasks', 'buffers', 'outside sources']))

        typeLabel = LabelSet(x='x', y='y', text='values', level='glyph',
                             x_offset=0, y_offset=0, source=source, render_mode='canvas', text_font_size="10pt")
        plot.add_layout(typeLabel)

        output_file('graph.html')
        show(plot)

        return None

def getLargePalette(size, palette):
    if size < 256:
        return palette[size]
    p = palette[:256]
    out = []
    for i in range(size):
        idx = int(i * 256.0 / size)
        out.append(p[idx])
    return out
