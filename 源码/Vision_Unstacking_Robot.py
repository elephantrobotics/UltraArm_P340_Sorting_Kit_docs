# import cv2 as cv
# import numpy as np
from pymycobot.ultraArm import ultraArm
import time
import serial
import serial.tools.list_ports

class Vision_Unstacking_Robot():
    def __init__(self,COM,robot_speed=100,pump_time=1) -> None:
        """
        COM: 机械臂的串口号;
        robot_speed: 机械臂运动速度;
        pump_time: 吸盘开关延时;
        """
       
        self.ua = None      
        self.angles = [              
            [-66.49, 13.12, -2.23,-25.3],#拆垛过渡点
            [-16.23, -11.9, -1.75,-25.3],  # 传送带过渡点            
           
           
        ]  

        self.coords = [
            [85.92, -247.08, 60,0], # 木块抓取点
            [219.52, -24.68, 60, 5], # 传送带放置点
                   
        ]

        self.time=pump_time    
        self.speed=robot_speed
        self.count=0
        self.lift_speed=50#Z轴抬升速度
        self.Z_flag=31#Z轴抬升偏移量
        self.ua = ultraArm(COM)
        self.pub_pump(False)
        # 确定好机械臂的串口号后，可把下面两行注释打开，重新上电后就无需使用myblockly回零，程序会自动回零
        # self.ua.go_zero() 
        # self.ua.sync()  
        self.ua.set_angles(self.angles[1],self.speed)
        
        self.ua.sync()
        
        
    # 控制吸泵
    def pub_pump(self, flag):
        if flag:
            self.ua.set_gpio_state(0)
        else:
            self.ua.set_gpio_state(1)

     #拆垛功能函数
    def move(self, x, y):                      
        print('real_x, real_y:', round(self.coords[0][0]+x, 2), round(self.coords[0][1]-y, 2))               
        self.ua.set_angles(self.angles[0], self.speed)
        self.ua.sync()              
        self.ua.set_coords([self.coords[0][0]+x, self.coords[0][1]-y, 134,self.coords[0][3]], self.speed)       
        self.ua.sync()       

        if -1<self.count<6:
            self.ua.set_coords([self.coords[0][0]+x, self.coords[0][1]-y,self.coords[0][2]-self.Z_flag*0,self.coords[0][3]], self.lift_speed)         
            self.ua.sync()
            
        elif 5<self.count<12:
            self.ua.set_coords([self.coords[0][0]+x, self.coords[0][1]-y,self.coords[0][2]-self.Z_flag*1,self.coords[0][3]], self.lift_speed)   
            self.ua.sync()
            
        elif 11<self.count<18:
            self.ua.set_coords([self.coords[0][0]+x, self.coords[0][1]-y,self.coords[0][2]-self.Z_flag*2,self.coords[0][3]], self.lift_speed)    
            self.ua.sync()

        elif self.count==18:
            self.count=0
        self.pub_pump(True)
        time.sleep(self.time)
        self.ua.set_coord("Z",134,self.lift_speed)
        self.count+=1 
        self.ua.sync()        
        self.ua.set_angles(self.angles[1], self.speed)
        self.ua.sync()       
        self.ua.set_coords([self.coords[1][0],self.coords[1][1],134,self.coords[1][3]],self.speed)
        self.ua.sync()
        self.ua.set_coords([self.coords[1][0],self.coords[1][1],self.coords[1][2],self.coords[1][3]],self.lift_speed)
        self.ua.sync()
        self.pub_pump(False)
        time.sleep(self.time) 
        self.ua.set_coord("Z",134,self.lift_speed)
        self.ua.sync()               
        self.ua.set_angles(self.angles[1],self.speed)
        self.ua.sync()


    def Special_handling(self,x,y,z):
        print("z=",z)
        print('real_x, real_y:', round(self.coords[0][0]+x, 2), round(self.coords[0][1]-y, 2))               
        self.ua.set_angles(self.angles[0], self.speed)
        self.ua.sync()              
        self.ua.set_coords([self.coords[0][0]+x, self.coords[0][1]-y, 134,self.coords[0][3]], self.speed)       
        self.ua.sync()       
        if 300<z<315:
            self.ua.set_coords([self.coords[0][0]+x, self.coords[0][1]-y,self.coords[0][2]-self.Z_flag*0,self.coords[0][3]], self.lift_speed)         
            self.ua.sync()
            
        elif 330<z<350:
            self.ua.set_coords([self.coords[0][0]+x, self.coords[0][1]-y,self.coords[0][2]-self.Z_flag*1,self.coords[0][3]], self.lift_speed)   
            self.ua.sync()
            
        elif 365<z<385:
            self.ua.set_coords([self.coords[0][0]+x, self.coords[0][1]-y,self.coords[0][2]-self.Z_flag*2,self.coords[0][3]], self.lift_speed)    
            self.ua.sync()

   
        self.pub_pump(True)
        time.sleep(self.time)
        self.ua.set_coord("Z",134,self.lift_speed)
  
        self.ua.sync()        
        self.ua.set_angles(self.angles[1], self.speed)
        self.ua.sync()       
        self.ua.set_coords([self.coords[1][0],self.coords[1][1],134,self.coords[1][3]],self.speed)
        self.ua.sync()
        self.ua.set_coords([self.coords[1][0],self.coords[1][1],self.coords[1][2],self.coords[1][3]],self.lift_speed)
        self.ua.sync()
        self.pub_pump(False)
        time.sleep(self.time) 
        self.ua.set_coord("Z",134,self.lift_speed)
        self.ua.sync()               
        self.ua.set_angles(self.angles[1],self.speed)
        self.ua.sync()
        pass
        
        
       


 