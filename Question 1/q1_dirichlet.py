# -*- coding: utf-8 -*-
"""20B60130_TranHuuNhatHuy_Q1_Dirichlet.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1vjBV6NDd25ZevOx7Aj88dQY2sGPy-CkA
"""

import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits import mplot3d

# Initial state properties
dx = dy = d = 0.1
alpha = 100
Lx = Ly = L = 10
x = np.arange(0, Lx + dx, dx)
y = np.arange(0, Ly + dy, dy)
g = 9.8

# Simulation runtime properties
N_iter = 1000
X, Y = np.meshgrid(x, y)
T = np.zeros((len(x), len(y)))
fig = plt.figure()

# Function to initiate plot with temperature input T
def init_plt3D(T, zmin = -1, zmax = 0):
  ax = fig.add_subplot(projection = '3d')
  plot = ax.scatter(X, Y, T, c = T, cmap = 'jet')
  ax.set_xlabel('X')
  ax.set_ylabel('Y')
  ax.set_zlim(zmin, zmax)
  plt.colorbar(plot)

# Function to simulate steady-state condition (part 1)
def sim_Steady(T):
  T = np.zeros((len(x), len(y)))
  init_plt3D(T)                                 # Initial state handling
  plt.title("Initial state")
  plt.savefig("Initial state.jpg")              # Capturing initial state
  w = 1.5                                       # Relaxation coefficient (0 < w < 2)
  T[0, :] = T[:, 0] = T[-1, :] = T[:, -1] = 0   # Dirichlet boundary condition, fixed at 0
  # Commencing simulation
  while (True):
    T_min = T[len(x)//2, len(y)//2]             # Section's center, also lowest point
    for i in range(1, len(x) - 1):
      for j in range(1, len(y) - 1):
        # Calculate residue Rk for every iteration
        Rk = 1/4 * (T[i+1, j] + T[i-1, j] + T[i, j+1] + T[i, j-1] - g/alpha*(dx**2))
        # Replace the value of T[i, j] for next iteration by adding Rk
        T[i, j] = (1 - w) * T[i, j] + w * Rk;
    # When the difference of T_min between 2 consecutive iterations is negligible, we terminate the simulation
    if (abs(T_min - T[50, 50]) <= 0.0001):
      plt.clf()
      init_plt3D(T)
      plt.savefig("steady state.jpg")
      break
  
#def save():
#    os.system("ffmpeg -framerate 30 -y -ite shot%1d.jpg -vcodec mpeg4 -y Kai_Steady.mp4")

sim_Steady(T)