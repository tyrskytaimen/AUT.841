from spatialmath import SE3
import numpy as np
import sympy as sp

'''
Task 4:
A: Rotate the box 90 degrees around Z_world
B: Move the box 20cm along the X_box
'''

# 90 degrees to radian
theta = 90*np.pi/180

# T4 = SE3.Rz(theta)  # A
# T4 = T4*SE3.Trans(20, 0, 0)  # B, also SE3.Tx(20)

T4 = SE3.Rz(theta)@SE3.Tx(20)
print(f"Task 4:\n{T4}")


'''
Task 5:
Rotate the box 90 degrees around Z_world
Move the box 20cm along the X_world
'''

T5 = SE3.Trans(20, 0, 0)*SE3.Rz(theta)
print(f"Task 5:\n{T5}")


'''
Task 6:
Rotate around X-axis by angle alpha
Translate along new X axis by a distance a
Translate along new Z axis by a distance d
Rotate around the new Z axis by an angle theta
'''

alpha, a, d, t = sp.symbols('alpha, a, d, t')

T6 = SE3.Rx(alpha)*SE3.Trans(a, 0, 0)*SE3.Trans(0, 0, d)*SE3.Rz(t)
print(f"Task 6:\n{T6}")
