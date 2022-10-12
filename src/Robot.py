from robodk.robolink import *  # API to communicate with RoboDK
from robodk.robomath import *       # import the robotics toolbox

class Robot:
    """
    Robot
    --------
    """
    robo_link : Robolink = None
    robo_ip : str = None
    robo_name : str = None
    dev : int

    def __init__(self):
        self._x = None

    def testing_rdk(self, RDK: Robolink):
        print("..       TESTING  INITIATED   ..")
        # print(RDK.ActiveStation().Name())
        print(self.robo_link.ActiveStation().Name())
        # print(self.robo_link.ActiveStation())
        print("..       TESTING  FISHED   ..")
        return 
        
