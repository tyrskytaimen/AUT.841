"""
Exercise 3
"""
import matplotlib.pyplot as plt
import numpy as np
from spatialmath import SE3

from roboticstoolbox import DHRobot, RevoluteMDH

from plotHelper import plotRobotAndFrame, conditional_teach

'''
MATLAB
script -> filename.m
run startup_rvc.m

L(1) = Link([0 0 0 0], 'modified')
L(2) = Link([0 0 .75 0])  %[theta d a alpha], theta is 0 even tho it is variable
two_link = SerialLink(L, 'name', 'two_link')
%%

%two_link.plot([0,0]) 
%you only see one link (L1)
%press sift to rotate camera
two_link.tool %gives tool matrix

two_link.teach([0,0])
%%

toolHT = transl(0.5, 0, 0)
toolLink.tool = toolHT
two_link.teach([0, 0])
'''

planarRobot = DHRobot(
    [
        RevoluteMDH(),
        RevoluteMDH(a=0.75)
    ]
    , name='planarRobot')

print("Robot:\n", planarRobot)

q = [0, 0]  # theta 1 and theta 2
# planarRobot.plot(q)
# plt.pause(600) # not needed for matplotlib version 3.8.0

# planarRobot.teach(q)

print("Tool:\n", planarRobot.tool)

toolHT = SE3(0.5, 0, 0)
planarRobot.tool = toolHT
planarRobot.teach(q)


# Forward kinematics
print("\n\nForward kinematics")
print(planarRobot.fkine([0, np.pi/2]))  # theta1=0, theta2=90 degrees


# Inverse kinematics
print("\n\nInverse kinematics")
target = SE3(0.75, 0.4, 0)
DOF = [1, 1, 0, 0, 0, 0]

print("iKine")
q_sol_1 = planarRobot.ikine_LM(target)
print("Success: ", str(q_sol_1.success), "\n")


print("iKine with mask")
q_sol_2 = planarRobot.ikine_LM(target, mask=DOF)
print("Success: ", str(q_sol_2.success), "\n")

print(planarRobot.fkine(q_sol_2.q))
planarRobot.plot(q_sol_2.q)
