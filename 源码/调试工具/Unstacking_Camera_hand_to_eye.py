
import sys
import os
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) 
sys.path.append(BASE_DIR) 
from Vision_Unstacking_Robot import *
from Unstacking_Camera import *
#请先阅读手册后，确定每个设备的串口号再运行此程序
if __name__=="__main__": 
    obj=Unstacking_Camera(cap_num=1,pump_x=-3,pump_y=-25)
    
    robot=Vision_Unstacking_Robot("COM8",robot_speed=150)
    data=obj.detect()
    while len(data)<6:
            print("二维码检测数目不对，请确保二维码在相机范围内并且能正确识别")
            time.sleep(1)
            data=obj.detect()          
        
    for i in range(len(data)):
        robot.hand_eye(data[i][2],data[i][1]) 
        sys.exit()
    
    