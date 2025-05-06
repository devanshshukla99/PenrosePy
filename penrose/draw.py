import numpy as np
import matplotlib.pylab as plt
from penrose.penrose import PenrosePy

length = 5
penrose = PenrosePy(length)
penrose.penrose_triangle()
r = np.linspace(-length, length, 100)
# t = np.sqrt(r**2 + 1)
# plot_hypersurface(r, t, structure, label=r"$t^2 - r^2 = 1$")
# t = np.sqrt(r**2 + 2)
# plot_hypersurface(r, t, structure, label=r"$t^2 - r^2 = 2$")

t = np.sqrt(1 + r**2) - 1
penrose.plot_hypersurface(r, t, label=r"$(t+1)^2 - r^2 = 1$")

t = np.sqrt(1 + r**2) - 2
penrose.plot_hypersurface(r, t, label=r"$(t+2)^2 - r^2 = 1$")

t = np.sqrt(1 + r**2) - 3
penrose.plot_hypersurface(r, t, label=r"$(t+3)^2 - r^2 = 1$")
penrose.show()

