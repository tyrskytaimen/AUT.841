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

print(scaraRobot)
scaraRobot.teach([0, 0, 0, 0])

exit()
