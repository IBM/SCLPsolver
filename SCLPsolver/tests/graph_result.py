from doe.data_generators.MCQN import generate_MCQN_data
from SCLP import SCLP, SCLP_settings
from bokeh.layouts import column
# select a palette
from bokeh.palettes import Dark2_5 as line_palette
from bokeh.palettes import Category20 as stacked_bar_chart_palette
import pandas as pd
from bokeh.core.properties import value
from bokeh.plotting import figure, show, output_file, gridplot
from bokeh.palettes import Category20
import math

from bokeh.io import show, output_file
from bokeh.plotting import figure
from bokeh.models import GraphRenderer, StaticLayoutProvider, Oval
from bokeh.palettes import Spectral8

# itertools handles the cycling
import itertools
import numpy as np

seed = 1000
number_of_buffers = 12
number_of_servers = 4
time_horizon = 150

G, H, F, gamma, c, d, alpha, a, b, TT, buffer_cost = generate_MCQN_data(seed, number_of_buffers, number_of_servers)
#vector alpha >0 , vector a can be any value
# a is input/output coming from outside
# alpha is initial value in buffer
# matrix G connected buffers and tasks
# in matrix G , flow between a task and multiple buffers
# task to buffer based on H[k,j] diagram 1
# a, buffer, task diagram 2


T = time_horizon
import time
start_time = time.time()
solver_settings = SCLP_settings(find_alt_line=False)
solution, STEPCOUNT, Tres, res = SCLP(G, H, F, a, b, c, d, alpha, gamma, T, solver_settings)
t, X, q, U, p, pivots, obj, err, NN, tau = solution.extract_final_solution()
print(obj, err)
time_to_solve = time.time() - start_time
print("--- %s seconds ---" % time_to_solve)
print("--- seed %s ---" % seed)
# we need to build nice plots for buffers status and time_slots utilization (look at bokeh: https://www.analyticsvidhya.com/blog/2015/08/interactive-data-visualization-library-python-bokeh/)
# Plots of buffers status: piecewise linear graphs where t = [0,t1,...,Tres] vector containing time partition and
#                           x - (12, len(t)) matrix representing quantities at each of 12 buffers at each timepoint
#                           lets start from separate plot for each buffer and see
# Plot of time_slots utilization:  4 barcharts where each bar can contain up to 12 colors. Colors are according to kind of tasks running on server
#                                we have 12 kinds of tasks (number of columns in H) and 4 time_slots (number of rows in H)
#                               if specific task (j) can run on the specific server (k) then we have H[k,j] > 0
#                               otherwise H[k,j] == 0 and we cannot run specific task on specific server
#                               U is a (16,len(t)-1) matrix where we interesting only on first (12,len(t)-1) part
#                               U[j,n] * H[k,j] indicate how many capacity of server k took task j at time period t[n]...t[n+1]
#                               we need for each server k create barchart where width of bar is length of time period
#                               and total height is sum(U[n,j] * H[k,j]) for all j this height splitted by different colors according to j (up to 12)


plot_width = 800
plot_height = 400



output_file("line.html")

plot_line = figure(plot_width=plot_width, plot_height=plot_height)

# create a color iterator
colors = itertools.cycle(line_palette)

# add a line renderer
for i,color in zip(range(number_of_buffers),colors):
    plot_line.line(t, X[i], line_width=2, line_color=color)

#show(plot_line)

number_of_time_slots = len(t)-1

output_file('stacked_area.html')
# create a color iterator
colors = stacked_bar_chart_palette[number_of_buffers]
print('colors = ',colors)

time_slots = ['t ' + str(i) for i in range(number_of_time_slots)]

tasks = ['task '+str(i) for i in range(1,len(H[0])+1)]
new_legend_tasks = {}
print('tasks=',tasks)

new_t = np.zeros(2 * number_of_time_slots)
new_t[0] = t[1]/2
new_t[1:-1] = np.repeat(t[1:-1],2)
new_t[-1] = t[-1]

data = {'t':new_t}

new_matrix = np.zeros((number_of_buffers,2 * number_of_time_slots))

p = {}
network_graph_tasks_indices = []
network_graph_server_indices = []
max_y_value = 1

for k in range(number_of_servers): # servers
    for j in range(number_of_buffers): # tasks
        for ti in range(0,number_of_time_slots): # time slices
            new_matrix[j, 2 * ti] = U[j, ti] * H[k, j]
            new_matrix[j, 2 * ti+1] = U[j, ti] * H[k, j]
        if H[k,j]>0:
            new_legend_tasks[j] = 'task '+str(j)
            network_graph_tasks_indices.append(j)
            network_graph_server_indices.append(len(tasks)+k)
            print('k,j=',k+1,',',j+1)
        data['task '+str(j+1)] = new_matrix[j].tolist()

    df = pd.DataFrame(data)

    #print('data = ',data)

    p[k] = figure(x_range=(0, time_horizon*1.2), y_range=(0, max_y_value),plot_width=plot_width, plot_height=plot_height, title='Server '+str(k)+' Utilization')

    p[k].varea_stack(stackers=tasks, x='t', color=Category20[number_of_buffers], legend=[value(x) for x in tasks], source=df)

    # reverse the legend entries to match the stacked order
    for j in reversed(range(number_of_buffers)):
        if H[k,j]==0:
            del p[k].legend[0].items[j]

    p[k].legend[0].items.reverse()

grid = gridplot([[p[0], p[1]], [p[2], p[3]]])
#show(grid)

from bokeh.io import show, output_file
from bokeh.plotting import figure
from bokeh.models import GraphRenderer, StaticLayoutProvider, Oval, Quad
from bokeh.palettes import Category20c

index_array_of_tasks = list(range(1,len(tasks)))
index_array_of_servers = list(range(len(tasks),len(tasks)+number_of_servers))

print('index_array_of_tasks=',index_array_of_tasks)
print('index_array_of_servers=',index_array_of_servers)

node_indices = np.concatenate((index_array_of_tasks,index_array_of_servers),axis=None).tolist()
node_x_location = np.concatenate((index_array_of_tasks,range(1,len(index_array_of_servers))),axis=None).tolist()
node_y_location = np.concatenate((np.full(len(index_array_of_tasks), 5),np.full(len(index_array_of_servers), 3)),axis=None).tolist()


plot = figure(title='Task to Server relationship', x_range=(0,len(node_indices)+1), y_range=(0,10),
              tools='', toolbar_location=None)

graph = GraphRenderer()

graph.node_renderer.data_source.add(node_indices, 'index')
graph.node_renderer.data_source.add(Category20c[len(node_indices)], 'color')
graph.node_renderer.glyph = Oval(height=1, width=1, fill_color='color')


print('start=',node_indices)
print('end=',node_y_location)

graph.edge_renderer.data_source.data = dict(
    start=list(network_graph_tasks_indices),
    end=list(network_graph_server_indices)
)

### start of layout code
#circ = [i*2*math.pi/8 for i in node_indices]
x = node_x_location
y = node_y_location

graph_layout = dict(zip(node_indices, zip(x, y)))
graph.layout_provider = StaticLayoutProvider(graph_layout=graph_layout)

plot.renderers.append(graph)

output_file('graph.html')
show(plot)


