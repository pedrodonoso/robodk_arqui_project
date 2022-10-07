
from robodk.robolink import *  # API to communicate with RoboDK
from robodk.robomath import *       # import the robotics toolbox

from robodk import *
from robolink import *

import os

# RDK = Robolink(
    
def connect_by_name(RDK: Robolink, name_robot: str, path_station: str, ):
    print("- Conectando..")

    ROBOT_IP = os.environ['ROBOT_IP']
    MAX_ATTEMPTS = int(os.environ['MAX_ATTEMPTS'])
    WAIT_CONNECTION = int(os.environ['WAIT_CONNECTION'])

    print("IP: ", ROBOT_IP)
    
    # modo de ejecucion
    # RDK.setRunMode(RUNMODE_RUN_ROBOT) 
    RDK.setRunMode(RUNMODE_SIMULATE)

    try:
        exist_path = RDK.getParam(param=FILE_OPENSTATION, str_type=True)
        print("exist: ", exist_path)
        if (type(exist_path) != 'str'):
            print("no existe variable de entorno.")
            RDK.AddFile(path_station)
            print("cargando archivo de configuración.")

        
        print("path station charged: ",RDK.getParam(param=FILE_OPENSTATION, str_type=True))

        # cargamos el robot importado en .rdk
        robot = RDK.Item(name_robot, ITEM_TYPE_ROBOT)
        print("name robot: ",robot.Name())

        print("ACTIVE_STATION: ", RDK.ActiveStation().Name())

        robot_connection = robot.ConnectSafe(robot_ip=ROBOT_IP, max_attempts=MAX_ATTEMPTS, wait_connection=WAIT_CONNECTION)

        if (robot_connection):
            print("- Conectado-")
            raise Exception("error")
        else:
            print("-NO Conectado-")
            # quit(0)

        # print("estado conexión: ", robot.ConnectedState()[1])  
        RDK.CloseRoboDK()
        print("Terminado")
        return
    except:
        quit()
        return
    finally:
        quit()
        return

    # movement_test(robot=robot)
    # RDK.ItemUserPick("Pick a robot", ITEM_TYPE_ROBOT)

    
    print(robot.Joints())
    # bien
    print("finalizado")


    # Load the CSV file as a list of list [[x,y,z,speed],[x,y,z,speed],...]
    # data = LoadList(path_file)
    # print(data)
    # Delete previously generated programs that follow a specific naming
    # Automatically delete previously generated items (Auto tag)
    # list_items = RDK.ItemList() # list all names
    # for item in list_items:
    #    if item.Name().startswith('Frame'):
    #        item.Delete()

    # Select the robot (the popup is diplayed only if there are 2 or more robots)
    # robot = RDK.ItemUserPick('Select a robot',ITEM_TYPE_ROBOT)
    # if not robot.Valid():
    #     raise Exception("Robot not selected or not valid")
    #     quit()
    quit()

    
