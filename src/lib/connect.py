from robodk.robolink import *  # API to communicate with RoboDK

def connect2robots(RDK):

    # gather all robots as item objects
    robots = RDK.ItemList(ITEM_TYPE_ROBOT, False)

    # loop through all the robots and connect to the robot
    errors = ''
    count = 0
    print("buscando...")
    print("robots: ", robots)
    if (len(robots) == 0):
        print("no hay robots.")
    for robot in robots:
        print("robot: ", robot)
        count = count + 1

        # force disconnect from all robots by simulating a double click
        #if count == 0:
        #    robot.Disconnect()
        #    robot.Disconnect()
        #    pause(1)

        # Important, each robot needs a new API connection to allow moving them separately in different threads (if required)
        rdk = Robolink()
        robot.link = rdk

        # Force simulation mode in case we are already connected to the robot.
        # Then, gather the joint position of the robots.
        # This will gather the position of the simulated robot instead of the real robot.
        rdk.setRunMode(RUNMODE_SIMULATE)
        jnts = robot.Joints()

        # connect to the robot:
        # rdk.setRunMode(RUNMODE_RUN_ROBOT) # not needed because connect will automatically do it
        # state = robot.ConnectSafe()
        state = robot.Connect()
        print(state)

        # Check the connection status and message
        state, msg = robot.ConnectedState()
        print(state)
        print(msg)
        if state != ROBOTCOM_READY:
            errors = errors + 'Problems connecting: ' + robot.Name() + ': ' + msg + '\n'
        else:
            # move to the joint position in the simulator:
            # robot.MoveJ(jnts, False)
            return robot

    # Display connection errors, if any
    if len(errors) > 0:
        print(errors)
        raise Exception(errors)
    else:
        quit(0)

    