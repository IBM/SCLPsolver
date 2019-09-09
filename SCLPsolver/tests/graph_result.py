from doe.data_generators.MCQN import generate_MCQN_data
from SCLP import SCLP, SCLP_settings
from bokeh.plotting import figure, output_file, show
from bokeh.core.properties import value
from bokeh.models import ColumnDataSource
# select a palette
from bokeh.palettes import Dark2_5 as line_palette
from bokeh.palettes import Category20 as stacked_bar_chart_palette
from bokeh.models import Legend
# itertools handles the cycling
import itertools
import numpy as np

seed = 1000
number_of_buffers = 12
number_of_servers = 4
time_horizon = 150

G, H, F, gamma, c, d, alpha, a, b, TT, buffer_cost = generate_MCQN_data(seed, number_of_buffers, number_of_servers)
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
# we need to build nice plots for buffers status and servers utilization (look at bokeh: https://www.analyticsvidhya.com/blog/2015/08/interactive-data-visualization-library-python-bokeh/)
# Plots of buffers status: piecewise linear graphs where t = [0,t1,...,Tres] vector containing time partition and
#                           x - (12, len(t)) matrix representing quantities at each of 12 buffers at each timepoint
#                           lets start from separate plot for each buffer and see
# Plot of servers utilization:  4 barcharts where each bar can contain up to 12 colors. Colors are according to kind of tasks running on server
#                                we have 12 kinds of tasks (number of columns in H) and 4 servers (number of rows in H)
#                               if specific task (j) can run on the specific server (k) then we have H[k,j] > 0
#                               otherwise H[k,j] == 0 and we cannot run specific task on specific server
#                               U is a (16,len(t)-1) matrix where we interesting only on first (12,len(t)-1) part
#                               U[j,n] * H[k,j] indicate how many capacity of server k took task j at time period t[n]...t[n+1]
#                               we need for each server k create barchart where width of bar is length of time period
#                               and total height is sum(U[n,j] * H[k,j]) for all j this height splitted by different colors according to j (up to 12)

output_file("line.html")

plot_width = 800
plot_height = 400

plot_line = figure(plot_width=plot_width, plot_height=plot_height)

# create a color iterator
colors = itertools.cycle(line_palette)

# add a line renderer
for i,color in zip(range(number_of_buffers),colors):
    plot_line.line(t, X[i], line_width=2, line_color=color)

show(plot_line)


# create a color iterator
colors = stacked_bar_chart_palette[12]

servers = ['server '+str(i) for i in range(1,len(H)+1)]
tasks = ['task '+str(i) for i in range(1,len(H[0])+1)]
print('colors = ',colors)


print('tasks=',tasks)

data = {'servers' : servers}

new_matrix = np.zeros((12,4))

for j in range(12):
    for k in range(4):
        new_matrix[j,k] = U[j,k]*H[k,j]
    data['task '+str(j+1)] = new_matrix[j].tolist()


print('data = ',data)

output_file("stacked.html")

width_array = t.tolist()[:13]
width_array = np.diff(width_array)

total_width = int(np.sum(width_array))

width_array = np.multiply(1/total_width, width_array).tolist()
print('width_array = ',width_array)


p = figure(x_range=servers, plot_height=plot_height, plot_width=plot_width, title="Server utilization by task",
           toolbar_location=None, tools="")

p.vbar_stack(tasks, x='servers', width=width_array, color=colors, source=data,
             legend=[value(x) for x in tasks])

p.legend.location = (0, 20)

show(p)