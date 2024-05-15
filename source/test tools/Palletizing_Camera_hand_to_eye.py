
import sys
import os
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) 
sys.path.append(BASE_DIR) 
from Palletizing_Robot import*
from Palletizing_Camera import *

if __name__=="__main__": 
    
    cam=Palletizing_Camera(cap_num=1,pump_x=30,pump_y=16)
   
    robot2=Palletizing_Robot("COM10",robot_speed=150,x_shift=10,y_shift=10)

    pose=cam.detect()
    
    while len(pose)<1:
            print("The number of QR code detection is wrong. Please ensure that the QR code is within the range of the camera and can be recognized correctly.")
            time.sleep(1)
            pose=cam.detect()         
        
    for i in range(1):
        id=robot2.hand_eye(pose[0],pose[1],pose[2],pose[3])
        sys.exit(0)
    