# add private modules
import sys
sys.path.append('../src/')
sys.path.append('./src/')

# flask modules
from flask import Flask, request, json

# configurations flask
import src.configuration as config
import src.responses as res

# import specific modules
from Movements import Movements as m
from Connections import Connections as c
from Robot import Robot as r

# robodk modules
from robodk import *  # API to communicate with RoboDK

# RDK = robolink.Robolink()

DEV = config.DEV
PATH_STATION = config.PATH_STATION
ROBOT_IP = config.ROBOT_IP

robot = r()

if (DEV == 1):
    print("DEV")
    robot.robo_link = robolink.Robolink()
else:
    print("PRODUCTION")
    robot.robo_link = robolink.Robolink(args=['-NOSPLASH','-HIDDEN'])
    robot.robo_link.setWindowState(windowstate=-1)

# robot = r()
# robot.robo_link = robolink.Robolink()

app = Flask(__name__)

@app.route("/setparams", methods=['POST'])
def setParams():
    print("hola")
    content_type = request.headers.get('Content-Type')
    if (content_type == 'application/json'):
        json = request.json
        print(request.json)
        r.robo_ip = str(json['ROBOT_IP'])
        r.robo_name = str(json['ROBOT_NAME'])
        # max_attempts = int(json['MAX_ATTEMPTS'])
        # wait_connection = int(json['WAIT_CONNECTION'])
        # dev = int(json['DEV'])
        # return json
        return res.response_ok
    else:
        return 'Content-Type not supported!'
    
@app.route("/test/connection")
def test_connection():
    robot.testing_rdk(RDK=robot.robo_link)
    # connection = c()


@app.route("/connection")
def connect():
   
    
    # revisar si existen las variables
    print(robot.robo_ip, robot.robo_name, PATH_STATION)
    if (robot.robo_ip is None or robot.robo_name is None or PATH_STATION is None) : return res.response_wrong_ip_robot 
    return res.response_ok
    
    
    # connection.connect_ip(RDK=robot.robo_link, name_robot=robot.robo_name, path_station=PATH_STATION, robot_ip=robot.robo_ip)
    # r.testing_rdk(RDK)
    # return response_ok
    
@app.route("/")
def hello():
    return "<p>Hello, World!</p>"

app.run(host='localhost', port=5000, debug=True)