from roboticstoolbox import DHRobot, RevoluteMDH

#Defining the robot
planarRobot = DHRobot(
    [
        RevoluteMDH(),
        RevoluteMDH(a=0.75),
    ], name="planarRobot")

print(planarRobot)
