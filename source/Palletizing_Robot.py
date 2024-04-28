from pymycobot.ultraArm import ultraArm
import time
import serial
import serial.tools.list_ports

class Palletizing_Robot():
    def __init__(self,COM,robot_speed=100,x_shift=50,y_shift=-50,pump_time=1) -> None:
        """
        COM: The serial port number of the robotic arm;
        robot_speed: Robot arm movement speed;
        x_shift:The Palletizing spacing of the center point of the wooden block grabbing in the X-axis direction;
        y_shift:The Palletizing spacing of the center point of the wooden block grabbing in the Y-axis direction;
        pump_time: Delay of suction cup switch
        """
        self.ua = None
        self.angles = [        
            [15.53, 3.83, -1.75,0],#Transition point
            [56.53, 4.83, -1.75,-25.3],#Transition lifting point in the Palletizing area
            
             [-18, 0, 0, -38]
            
        ]

        self.coords = [
            [207.3, 102.25, 59, -38], # Camera capture initialization point
            
            [-13.13, 277.26, 0, 38],#Palletizing position point
          
            ]
        
        self.angel_reversal=-142
        
        self.speed=robot_speed
        self.time=pump_time
        self.x_shif=30+x_shift#X-axis offset
        self.y_shif=-(30+y_shift)#Y-axis offset
        self.a_flag=self.b_flag=self.c_flag=self.d_flag=self.e_flag=self.f_flag=0
        self.count=0
        self.lift_speed=50#Z-axis lifting speed
        self.Z_flag=31#Z-axis lifting offset       
        self.ua = ultraArm(COM)
        self.pub_pump(False)  
        # After determining the serial port number of the robotic arm, you can open the following two lines of comments. After powering on again, there is no need to use myblockly to return to zero, and the program will automatically return to zero
        # self.ua.go_zero() 
        # self.ua.sync()   
        self.ua.set_angles(self.angles[3], self.speed)
        self.ua.sync()
        



          
    def pub_pump(self, flag):
        if flag:
            self.ua.set_gpio_state(0)
        else:
            self.ua.set_gpio_state(1)

    
   
    

    def move(self, x, y, yaw,id):                     
        print('real_x, real_y:', round(self.coords[0][0]+x, 2), round(self.coords[0][1]+y, 2))  
        self.ua.set_angles(self.angles[3], self.speed)
        self.ua.sync()      
        self.ua.set_coords([self.coords[0][0]+x, self.coords[0][1]+y, 134,yaw], self.lift_speed)
        self.ua.sync()       
        self.ua.set_coords([self.coords[0][0]+x, self.coords[0][1]+y,self.coords[0][2],yaw], self.lift_speed)
        self.ua.sync()       
        self.pub_pump(True)
        time.sleep(1)       
        self.ua.set_coord("Z",134,self.lift_speed)
        self.ua.sync()
        self.ua.set_coords([self.coords[0][0]+x, self.coords[0][1]+y, 134,self.coords[0][3]], self.lift_speed)
        self.ua.sync()              
        return id                 

    

    def judge(self,id):
        if 0< id <4 :                 
            self.ua.set_angles(self.angles[1],self.speed)
            self.ua.sync()
            self.ua.set_coords([self.coords[1][0],self.coords[1][1],134,self.coords[1][3]],self.speed)
            self.ua.sync()
            self.ua.set_coords([self.coords[1][0],self.coords[1][1],self.coords[1][2]+self.a_flag*self.Z_flag,self.coords[1][3]],self.lift_speed)
            self.ua.sync()
            self.pub_pump(False)
            time.sleep(self.time)
            self.ua.set_coord("Z",134,self.lift_speed)
            self.ua.sync()
            self.a_flag+=1
            self.count+=1
            self.ua.set_angles(self.angles[1],self.speed)
            self.ua.sync()

        elif 3< id <7 :
            self.ua.set_angles(self.angles[1],self.speed)
            self.ua.sync()
            self.ua.set_coords([self.coords[1][0]+self.x_shif,self.coords[1][1],134,self.coords[1][3]],self.speed)
            self.ua.sync()
            self.ua.set_coords([self.coords[1][0]+self.x_shif,self.coords[1][1],self.coords[1][2]+self.b_flag*self.Z_flag,self.coords[1][3]],self.lift_speed)
            self.ua.sync()
            self.pub_pump(False)
            time.sleep(self.time)
            self.ua.set_coord("Z",134,self.lift_speed)
            self.ua.sync()
            self.b_flag+=1
            self.count+=1
            self.ua.set_angles(self.angles[1],self.speed)
            self.ua.sync()

        elif 6< id <10 :
            self.ua.set_angles(self.angles[1],self.speed)
            self.ua.sync()
            self.ua.set_coords([self.coords[1][0]+self.x_shif*2,self.coords[1][1],134,self.coords[1][3]],self.speed)
            self.ua.sync()
            self.ua.set_coords([self.coords[1][0]+self.x_shif*2,self.coords[1][1],self.coords[1][2]+self.c_flag*self.Z_flag,self.coords[1][3]],self.lift_speed)
            self.ua.sync()
            self.pub_pump(False)
            time.sleep(self.time)
            self.ua.set_coord("Z",134,self.lift_speed)
            self.ua.sync()
            self.c_flag+=1
            self.count+=1
            self.ua.set_angles(self.angles[1],self.speed)
            self.ua.sync()


        elif 9< id <13 :
            self.ua.set_angles(self.angles[1],self.speed)
            self.ua.sync()
            self.ua.set_coords([self.coords[1][0],self.coords[1][1]+self.y_shif,134,self.angel_reversal],self.speed)
            self.ua.sync()
            self.ua.set_coords([self.coords[1][0],self.coords[1][1]+self.y_shif,self.coords[1][2]+self.d_flag*self.Z_flag,self.angel_reversal],self.lift_speed)
            self.ua.sync()
            self.pub_pump(False)
            time.sleep(self.time)
            self.ua.set_coord("Z",134,self.lift_speed)
            self.ua.sync()
            self.d_flag+=1
            self.count+=1
            self.ua.set_angles(self.angles[1],self.speed)
            self.ua.sync()

        elif 12< id <16 :
            self.ua.set_angles(self.angles[1],self.speed)
            self.ua.sync()
            self.ua.set_coords([self.coords[1][0]+self.x_shif,self.coords[1][1]+self.y_shif,134,self.angel_reversal],self.speed)
            self.ua.sync()
            self.ua.set_coords([self.coords[1][0]+self.x_shif,self.coords[1][1]+self.y_shif,self.coords[1][2]+self.e_flag*self.Z_flag,self.angel_reversal],self.lift_speed)
            self.ua.sync()
            self.pub_pump(False)
            time.sleep(self.time)
            self.ua.set_coord("Z",134,self.lift_speed)
            self.ua.sync()
            self.e_flag+=1
            self.count+=1
            self.ua.set_angles(self.angles[1],self.speed)
            self.ua.sync()

        elif 15< id <19 :
            self.ua.set_angles(self.angles[1],self.speed)
            self.ua.sync()
            self.ua.set_coords([self.coords[1][0]+self.x_shif*2,self.coords[1][1]+self.y_shif,134,self.angel_reversal],self.speed)
            self.ua.sync()
            self.ua.set_coords([self.coords[1][0]+self.x_shif*2,self.coords[1][1]+self.y_shif,self.coords[1][2]+self.f_flag*self.Z_flag,self.angel_reversal],self.lift_speed)
            self.ua.sync()
            self.pub_pump(False)
            time.sleep(self.time)
            self.ua.set_coord("Z",134,self.lift_speed)
            self.ua.sync()
            self.f_flag+=1
            self.count+=1
            self.ua.set_angles(self.angles[1],self.speed)
            self.ua.sync()
        self.ua.set_angles(self.angles[3], self.speed)
        self.ua.sync() 




   



        

