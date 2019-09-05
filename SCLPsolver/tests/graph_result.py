from doe.data_generators.MCQN import generate_MCQN_data
from SCLP import SCLP, SCLP_settings
from bokeh.plotting import figure, output_file, show
# select a palette
from bokeh.palettes import Dark2_5 as palette
# itertools handles the cycling
import itertools

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
t, X, q, u, p, pivots, obj, err, NN, tau = solution.extract_final_solution()
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
#                               u is a (16,len(t)-1) matrix where we interesting only on first (12,len(t)-1) part
#                               u[n,j] * H[k,j] indicate how many capacity of server k took task j at time period t[n]...t[n+1]
#                               we need for each server k create barchart where width of bar is length of time period
#                               and total height is sum(u[n,j] * H[k,j]) for all j this height splitted by different colors according to j (up to 12)

output_file("line.html")

p = figure(plot_width=800, plot_height=400)

# create a color iterator
colors = itertools.cycle(palette)

# add a line renderer
for i,color in zip(range(number_of_buffers),colors):
    p.line(t, X[i], line_width=2, line_color=color)

show(p)

# output_file("barchart.html")
#
#
# for i,color in zip(range(number_of_buffers),colors):
#     p.vbar(x=H[i], width=0.5, bottom=0,
#        top=[1.2, 2.5, 3.7], color=color)
