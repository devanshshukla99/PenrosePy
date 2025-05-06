import numpy as np
import matplotlib.pylab as plt
from matplotlib import transforms
from penrose.penrose import PenrosePy

length = np.pi/2
penrose = PenrosePy(length)
penrose.penrose_triangle()
r = np.linspace(-(2*length), (2*length), 1000)
# t = np.sqrt(r**2 + 0.5**2)
# penrose.plot_hypersurface(r, t, label=r"$t^2 - r^2 = 0.5^2$")
# t = np.sqrt(r**2 + 0.2**2)
# penrose.plot_hypersurface(r, t, label=r"$t^2 - r^2 = 0.2^2$")
# t = np.sqrt(r**2 + 1)
# penrose.plot_hypersurface(r, t, label=r"$t^2 - r^2 = 1$")
# t = np.sqrt(r**2 + 1.2**2)
# penrose.plot_hypersurface(r, t, label=r"$t^2 - r^2 = 1.2^2$")

t = np.sqrt(1 + r**2) - 0.4
penrose.plot_hypersurface(r, t, label=r"$(t+0.4)^2 - r^2 = 1$")

t = np.sqrt(1 + r**2) - 1
penrose.plot_hypersurface(r, t, label=r"$(t+1)^2 - r^2 = 1$")

t = np.sqrt(1 + r**2) - 2
penrose.plot_hypersurface(r, t, label=r"$(t+2)^2 - r^2 = 1$")

# t = np.sqrt(1 + r**2) - 3
# t = r
# penrose.plot_hypersurface(r, t, label=r"$(t+3)^2 - r^2 = 1$")
penrose.show()

# # x = 0 plot
# x = np.linspace(-10, 10, 400)
# y = np.zeros_like(x)

# # Rotation matrix for 45 degrees
# theta = np.radians(45)  # Convert angle to radians
# rotation_matrix = np.array([[np.cos(theta), -np.sin(theta)],
#                             [np.sin(theta), np.cos(theta)]])

# # Apply the rotation to the x, y coordinates
# rotated_coordinates = np.dot(rotation_matrix, np.array([x, y]))

# # Extract the rotated x and y values
# x_rotated, y_rotated = rotated_coordinates

# # Create the plot
# fig, ax = plt.subplots()
# ax.plot(x, y, label="Rotated Line", color='C1')
# ax.plot(x_rotated, y_rotated, label="Rotated Line", color='blue')

# # Add labels and title
# ax.set_title("Rotated Line Plot by 45 Degrees")
# ax.set_xlabel("x")
# ax.set_ylabel("y")

# # Add a grid
# ax.grid(True)

# # Show the plot
# ax.legend()
# plt.show()
