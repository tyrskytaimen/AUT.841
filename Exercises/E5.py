import numpy as np
from spatialmath import SE3
from roboticstoolbox import DHRobot, RevoluteMDH, PrismaticMDH

scaraRobot = DHRobot(
    [
        RevoluteMDH(d=0.9),
        RevoluteMDH(a=0.4),
        RevoluteMDH(a=0.5),
        PrismaticMDH(alpha=np.pi,
                     qlim=[-1, 1])
    ]
    , name='scaraRobot')

scaraRobot.base = SE3(0.1, 0.1, 0.2)
scaraRobot.tool = SE3(0, 0, 0.135)

print(scaraRobot)
print("Base:\n", scaraRobot.base)
print("Tool:\n", scaraRobot.tool)
print("Green target:\n", SE3.Trans(0.6, 0.6, 0)@SE3.Rz(45, unit='deg'))
print("Red target:\n", SE3.Trans(0.3, 0.8, 0.1))

scaraRobot.teach([0, 0, 0, 0])

exit()
