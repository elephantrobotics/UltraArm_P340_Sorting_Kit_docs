from Vision_Unstacking_Robot import *
from Unstacking_Camera import *
from ConveyorMain import *
from Palletizing_Robot import *
import sys
from Palletizing_Camera import *
from Message import *


if __name__=="__main__": 
    
    obj=Unstacking_Camera(cap_num=2,pump_x=-6,pump_y=-23)
    cam=Palletizing_Camera(cap_num=1,pump_x=8,pump_y=5)
    robot=Vision_Unstacking_Robot("COM26",robot_speed=100)
    robot2=Palletizing_Robot("COM20",robot_speed=100,x_shift=10,y_shift=10)
    conveyer=ConveyorMain("COM21")
    
    for i in range(4):
        data=obj.detect_color()
        robot.move_color(data[1],data[0])
        conveyer.open_conveyor(50)
        time.sleep(5)
        conveyer.close_conveyor()
        pose=cam.detect_color()
        id=robot2.move(pose[0],pose[1],pose[2],pose[3])                   
        robot2.color_judge(id) 

       

        
    
