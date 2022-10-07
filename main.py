from robodk.robolink import *  # API to communicate with RoboDK
from robodk.robomath import *  # basic matrix operations

import src.connect as connect
import src.move as move
import src.connect_by_name as cbn

from dotenv import load_dotenv
import os

load_dotenv()

DEV = int(os.environ['DEV'])

print("DEV: ", DEV)

if (DEV == 1):
    print("DEV")
    RDK = Robolink()
else:
    print("PRODUCTION")
    RDK = Robolink(args=['-NOSPLASH','-HIDDEN'])
    RDK.setWindowState(windowstate=-1)



PATH_STATION = "C:/Users/pedro/OneDrive - Universidad Técnica Federico Santa María/External-projects/robodk_arqui/rdk_files/arqui_robot.rdk"
cbn.connect_by_name(RDK, name_robot="UR5", path_station=PATH_STATION)

# robot = connect.connect2robots(RDK)
# print("conectado terminado")
# move.moverobot(RDK, robot)
# cbn.movement_test()