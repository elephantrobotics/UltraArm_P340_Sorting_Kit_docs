from pymycobot.ultraArm import ultraArm
import time
import serial
import serial.tools.list_ports

class Palletizing_Robot():
    def __init__(self,COM,robot_speed=100,x_shift=50,y_shift=-50,pump_time=1) -> None:
        """
        COM: 机械臂的串口号;
        robot_speed: 机械臂运动速度;
        x_shift:木块抓取中心点在X轴方向的码垛间距;
        y_shift:木块抓取中心点在Y轴方向的码垛间距;
        pump_time: 吸盘开关延时
        """
        self.ua = None
        self.angles = [        
            [15.53, 3.83, -1.75,0],#过渡点
            [56.53, 4.83, -1.75,-25.3],#码垛区域过渡抬高点
            [56.53, 4.83, -1.75,-25.3],#码垛区域过渡抬高点
             [-18, 0, 0, -38]
            
        ]

        self.coords = [
            [207.3, 102.25, 59, -38], # 相机抓取初始化点
            #  [207.3, 102.25, 102, -38], # 相机抓取初始化点
            [-13.13, 277.26, 0, 38],#码垛位置点
           # [-13.13, 277.26, 11.0, 38],#香港展会码垛位置点
            ]
        
        self.angel_reversal=-142
        
        self.speed=robot_speed
        self.time=pump_time
        self.x_shif=30+x_shift#X轴方向偏移
        self.y_shif=-(30+y_shift)#Y轴方向偏移
        self.a_flag=self.b_flag=self.c_flag=self.d_flag=self.e_flag=self.f_flag=0
        self.count=0
        self.lift_speed=50#Z轴抬升速度
        self.Z_flag=31#Z轴抬升偏移量       
        self.ua = ultraArm(COM)
        self.pub_pump(False)  
        # 确定好机械臂的串口号后，可把下面两行注释打开，重新上电后就无需使用myblockly回零，程序会自动回零
        # self.ua.go_zero() 
        # self.ua.sync()   
        self.ua.set_angles(self.angles[3], self.speed)
        self.ua.sync()
        



    # 控制吸泵      
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




   



        

