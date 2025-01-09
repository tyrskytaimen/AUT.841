import matplotlib.pyplot as plt
import numpy as np
from spatialmath import SE3

from roboticstoolbox import DHRobot, RevoluteMDH, PrismaticMDH

from plotHelper import plotRobotAndFrame, conditional_teach

enable_teach = False

# *** Case 2 RRR positive – CCW, P positive - DOWN
scaraRobot = DHRobot(
    [
        RevoluteMDH(d=0.5),
        RevoluteMDH(a=0.4),
        RevoluteMDH(a=0.3),
        PrismaticMDH(alpha=np.pi,qlim=[-1, 1]),
    ], name="scaraRobot")
print(scaraRobot)

# Plot the robot using the teach command
conditional_teach(scaraRobot, [0,0,0,0], enable_teach)

print(scaraRobot.base)

#Important: move the robot base closer to the targets
baseHT = SE3(0.1, 0.1, 0.2)
scaraRobot.base = baseHT

conditional_teach(scaraRobot, [0,0,0,0], enable_teach)


#Tool property
print(scaraRobot.tool)

toolHT = SE3(-0.03,0,0.135) #create the HT matrix of the tool
scaraRobot.tool = toolHT   #add the tool to the robot
print("Scara robot tool")
print(scaraRobot.tool)
conditional_teach(scaraRobot, [0,0,0,0], enable_teach)   #Robot is plotted with  0 joint variables

# *****************

# Some target
someTarget = SE3(1,1,.5)
print("Plot green target")
plotRobotAndFrame(scaraRobot, [0,0,0,0], green_target, plt)

# q=scaraRobot.ikine_LM(red_target_fixed,mask=[?])
