from robodk.robolink import *  # API to communicate with RoboDK
from robodk.robomath import *       # import the robotics toolbox

import lib.connect_by_name as connect_bn

class Connections:    
    """
    Conexiones a RDK
    -----------
    """
    robotlink = Robolink()
    testee = "ola"

    def __init__(self):
        self._x = None
        
    def set_robot_connection(self, new_connection):
        setattr(self, '_' + 'testee', new_connection)
        print(getattr(self, '_' + 'testee'))

    def connect_ip(self, RDK: Robolink, name_robot: str, path_station: str, robot_ip: str):
        """
        Conectar a robot con IP.
        ----------
        RDK : Robolink
            -
        name_robot : str
            Nombre del robot importado en el archivo .rdk
        path_station : str
            Dirección del directorio del archivo .rdk de configuración.
        robot_ip : str
            -
        """
        connect_bn.connect_by_name(RDK, name_robot, path_station, robot_ip)
        return True