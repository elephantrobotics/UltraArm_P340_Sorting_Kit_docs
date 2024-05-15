
import sys
import os
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) 
sys.path.append(BASE_DIR) 
from Vision_Unstacking_Robot import *
from Unstacking_Camera import *

if __name__=="__main__": 
    obj=Unstacking_Camera(cap_num=2,pump_x=-3,pump_y=-25)
    
    robot=Vision_Unstacking_Robot("COM12",robot_speed=150)
    data=obj.detect()
    while len(data)<6:
            print("The number of QR code detection is wrong. Please ensure that the QR code is within the range of the camera and can be recognized correctly.")
            time.sleep(1)
            data=obj.detect()          
        
    for i in range(len(data)):
        robot.hand_eye(data[i][2],data[i][1]) 
        sys.exit()
    
    