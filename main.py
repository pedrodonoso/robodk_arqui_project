from robodk.robolink import *  # API to communicate with RoboDK
# from robodk.robomath import *  # basic matrix operations

import src.connect as connect
import src.move as move

RDK = Robolink()

# connect.connect2robots(RDK)
move.moverobot(RDK)