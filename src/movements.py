from robodk.robolink import *  # API to communicate with RoboDK
from robodk.robomath import *       # import the robotics toolbox

import lib.move as move
import lib.move_test as move_test

class Movements:
    """
    Movimientos robodk
    -----------
    """
    def __init__(self):
        self._x = None
    def moverobotWASD(RDK, robot):
        move.moverobot(RDK, robot)
    def movement_test(robot):
        move_test(robot)