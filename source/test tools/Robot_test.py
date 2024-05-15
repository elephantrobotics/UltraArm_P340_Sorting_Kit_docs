from pymycobot.ultraArm import ultraArm
import time
robot1 = ultraArm("COM12")
robot2 = ultraArm("COM10")
# robot1.set_angle()
def check_robot(ua):
    ua.go_zero()    
    ua.sync()   
    ua.set_angle(4,90,100)   
    ua.sync()
    ua.set_gpio_state(0)
    time.sleep(2)
    ua.set_gpio_state(1)
    time.sleep(1)
   


check_robot(robot1)
check_robot(robot2)
