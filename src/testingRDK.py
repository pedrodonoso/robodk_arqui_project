from robodk.robolink import *  # API to communicate with RoboDK

def testing_rdk(RDK: Robolink):
    print("..       TESTING  INITIATED   ..")
    print(RDK.ActiveStation())
    print("..       TESTING  FISHED   ..")
    return 