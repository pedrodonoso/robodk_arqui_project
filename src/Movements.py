from robodk.robolink import *  # API to communicate with RoboDK
from robodk.robomath import *       # import the robotics toolbox

# import lib.move as move
import lib.move_test as move_test


def moverobotWASD(RDK, robot):
    print("algo")
    # move.moverobot(RDK, robot)
def movement_test(robot):
    move_test(robot)
