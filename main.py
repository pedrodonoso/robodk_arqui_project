from robodk.robolink import *  # API to communicate with RoboDK
from robodk.robomath import *  # basic matrix operations

sys.path.append('./src/')

from Movements import Movements as m
from Connections import Connections as c
from lib import connect_by_name as cbn
# import src.lib.connect as connect
# import src.lib.move as move
# import src.lib.connect_by_name as cbn

# from src.Movements import Movements as m

from dotenv import load_dotenv
import os

load_dotenv()

DEV = int(os.environ['DEV'])

print("DEV: ", DEV)

if (DEV == 1):
    print("DEV")
    # RDK = Robolink(args=['-NOSPLASH','-HIDDEN'])
    
    # RDK = Robolink(args=['-NOSPLASH','-NOSHOW'])
    # RDK = Robolink(args=['NOSPLASH','NOSHOW'])
    RDK = Robolink(args=['/NOUI', '/NOSPLASH','/NOSHOW', '/HIDDEN', '/NO_WINDOWS'])
    RDK.setWindowState(windowstate=WINDOWSTATE_HIDDEN)
    RDK.HideRoboDK()
    # modo de ejecucion
    #RDK.setRunMode(RUNMODE_RUN_ROBOT)
else:
    print("PRODUCTION")
    RDK = Robolink(args=['/NOSPLASH','/NOSHOW'])
    RDK.setRunMode(RUNMODE_RUN_ROBOT) 

PATH_STATION = os.environ['PATH_STATION']
ROBOT_IP = os.environ['ROBOT_IP']

RDK, robot = cbn.connect_by_name(RDK=RDK, name_robot="UR5", path_station=PATH_STATION, robot_ip=ROBOT_IP)

# print("Conectado!!!!...")
# m.movement_test(RDK=RDK, robot=robot)
m.moverobotWASD(RDK=RDK, robot=robot)