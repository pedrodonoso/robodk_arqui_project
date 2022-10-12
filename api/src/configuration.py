from robodk.robolink import Robolink 
from dotenv import load_dotenv
import os

load_dotenv()

DEV = int(os.environ['DEV'])

# if (DEV == 1):
#     print("DEVELOPMENT")
#     RDK = Robolink()
# else:
#     print("PRODUCTION")
#     RDK = Robolink(args=['-NOSPLASH','-HIDDEN'])
#     RDK.setWindowState(windowstate=-1)

PATH_STATION = "C:/Users/pedro/OneDrive - Universidad Técnica Federico Santa María/External-projects/robodk_arqui/rdk_files/arqui_robot.rdk"
ROBOT_IP = os.environ['ROBOT_IP']