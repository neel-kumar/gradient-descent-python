# Use gradient descent to fit a line to a set of randomly generated points.

from bokeh.plotting import figure, show, output_file, save
import random
from datetime import datetime

# Co-efficients of a straight line
a_org = 5
b_org = 3

# Start of the line
x_start = 0

# End of the line
x_end = 10

# How far away the points can be from the line on the y axis
pm = 10

# How many points
n = 100

# The range of randomly generated x axis values
x_min = 0
x_max = 10

# Error limit
err_limit = 0.1

# Learning Rate
lr = 0.001

f = f = figure(width = 150, height = 150, title = "Gradient Decent", sizing_mode = "scale_width")

# Plotting the line on which you origanally made the scatterplot
def plot_line(a, b, x, x1, color):
    y = a * x + b
    y1 = a * x1 + b
    f.segment(x, y, x1, y1, color = color)

# Randomly generating the scatterplot
def gen_scatter(a, b, n, pm, x_min, x_max):
    points = []
    for i in range(0, n - 1):
        x2 = random.randint(x_min, x_max)
        py = a * x2 + b
        y2 = py - random.randint(-pm, pm)
        points.append((x2, y2))
    return points

# Plotting the randomly generated scatterplot
def plot_scatter(points):
    for xy in points:
        f.circle(xy[0], xy[1])

# The mean difference of the line's y value for a given x value compared to a point's, to the power 2
def err(a, b, points):
    avg_err = 0
    for xy in points:
        y = a * xy[0] + b
        avg_err = (y - xy[1]) ** 2 + avg_err
    avg_err = avg_err / len(points)
    return avg_err

# This calculates the slopes of the ag by error graph and the slope of the bg by error graph
def avg_slope_err(points, ag, bg):
    a_err = 0
    b_err = 0
    for xy in points:
        yg = ag * xy[0] + bg
        a_err = 2 * (yg - xy[1]) * xy[0] + a_err
        b_err = 2 * (yg - xy[1]) + b_err
    avg_a_err = a_err / len(points)
    avg_b_err = b_err / len(points)
    return [avg_a_err, avg_b_err]

# Plotting the line that the scatterplot is built around and plotting the scatterplot
plot_line(a_org, b_org, x_start, x_end, "Red")
points = gen_scatter(a_org, b_org, n, pm, x_min, x_max)
plot_scatter(points)

# declaring the variables for gradient decent
gd_a = random.randint(-x_max, x_max)
gd_b = random.random()
i = 0
max_i = 1000

print ("The Time at the start of gd is {}. gd_a = {}. gd_b = {}".format(datetime.now(), gd_a, gd_b))

# This is the part of the program that does gradient decent
while err(gd_a, gd_b, points) > err_limit and (i < max_i):
    i = i + 1
    ase = avg_slope_err(points, gd_a, gd_b)


    # This utilizes the avg_slpoe_err function
    gd_a = gd_a - ase[0] * lr
    gd_b = gd_b - ase[1] * lr

    # Plotting the line that each iteration ends up with
    plot_line(gd_a, gd_b, x_start, x_end, "Green")

    if i % 10000 == 0:
        print ("The Time at iteration # {} of gd is {}.".format(i, datetime.now()))

print ("The Time at the end of gd is {}. gd_a = {}. gd_b = {}".format(datetime.now(), gd_a, gd_b))

# Plotting the End product of gradient decent
plot_line(gd_a, gd_b, x_start, x_end, "Black")

print ("The original a is {} and the original b is {}. The error for these values are {}".format(a_org, b_org, err(a_org, b_org, points)))

output_file("GD.html")
save(f)

### Sample output
# The Time at the start of gd is 2019-05-25 10:19:34.542717. gd_a = 1. gd_b = 0.7369391386327541
# The Time at the end of gd is 2019-05-25 10:19:35.450703. gd_a = 5.034315927456152. gd_b = 2.103378366383095
# The original a is 5 and the original b is 3. The error for these values are 36.95959595959596
###
