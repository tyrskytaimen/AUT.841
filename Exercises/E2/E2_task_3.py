from spatialmath import SE3
import numpy as np

# 20 degrees to radian
theta = 20*np.pi/180

# Homogeneous transformation matrix for rotation around z-axis
T = SE3.Rz(theta)
print(T)
