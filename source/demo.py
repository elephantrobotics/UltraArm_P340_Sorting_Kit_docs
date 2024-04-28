from Vision_Unstacking_Robot import *
from Unstacking_Camera import *
from ConveyorMain import *
from Palletizing_Robot import *
import sys
from Palletizing_Camera import *
from Message import *

#Please read the manual first and determine the serial port number of each device before running this program
if __name__=="__main__": 
    obj=Unstacking_Camera(cap_num=1,pump_x=0,pump_y=-25)
    cam=Palletizing_Camera(cap_num=2,pump_x=40,pump_y=10)
    robot=Vision_Unstacking_Robot("COM12",robot_speed=150)
    robot2=Palletizing_Robot("COM8",robot_speed=150,x_shift=10,y_shift=10)
    conveyer=ConveyorMain("COM10")
    
    while robot2.count<18:
        data=obj.detect()
        while len(data)<6:
            print("The number of Aruco code detections is incorrect. Please ensure that the Aruco code is within the camera range and can be correctly recognized")
            time.sleep(1)
            data=obj.detect()          
        
        for i in range(len(data)):
            robot.move(data[i][2],data[i][1])                                  
            conveyer.open_conveyor(100)#Running speed of conveyor belt，speed:0-100
            time.sleep(5.2)          
            conveyer.close_conveyor()
            for i in range(3):
                try:
                    print("i=",i)                                
                    pose=cam.detect()
                    if pose is not None: 
                        break
                    
                except Exception as e:
                    if i==2:
                       message()                
                    temp=obj.exception_handling()
                    robot.Special_handling(temp[0][2],temp[0][1],temp[0][3])
                    conveyer.open_conveyor(100)
                    time.sleep(5.2)
                    conveyer.close_conveyor()
            id=robot2.move(pose[0],pose[1],pose[2],pose[3])                   
            robot2.judge(id)  
               

        
    
