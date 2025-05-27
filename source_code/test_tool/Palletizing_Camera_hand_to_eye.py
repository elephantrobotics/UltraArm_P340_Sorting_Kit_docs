
import sys
import os
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) 
sys.path.append(BASE_DIR) 
from Palletizing_Robot import*
from Palletizing_Camera import *
#请先阅读手册后，确定每个设备的串口号再运行此程序
if __name__=="__main__": 
    
    cam=Palletizing_Camera(cap_num=2,pump_x=30,pump_y=16)
   
    robot2=Palletizing_Robot("COM9",robot_speed=150,x_shift=10,y_shift=10)

    pose=cam.detect()
    
   
    # stepping_motor=Stepping_motor("COM14")
    while len(pose)<1:
            print("二维码检测数目不对，请确保二维码在相机范围内并且能正确识别")
            time.sleep(1)
            pose=cam.detect()         
        
    for i in range(1):
        id=robot2.hand_eye(pose[0],pose[1],pose[2],pose[3])
        sys.exit(0)
    