import htplpy as pl
import math

x_inds = range(-10,10)
x_vals = [xi/10.0 for xi in x_inds]
y_vals = [math.exp(-x*x) for x in x_vals]
x2 = [2*x for x in x_vals]

pl.plot(x_vals, y_vals, '-o')
pl.plot(x_vals, x_vals, 'o')
pl.plot(x_vals, x2)

pl.show()
