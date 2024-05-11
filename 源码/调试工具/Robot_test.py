from pymycobot.ultraArm import ultraArm
import time
robot1 = ultraArm("COM8")
robot2 = ultraArm("COM9")

def check_robot(ua):
    ua.go_zero()
    ua.sync()
    ua.set_angle(4,90)
    ua.sync()
    ua.set_gpio_state(0)
    time.sleep(2)
    ua.set_gpio_state(1)
    time.sleep(1)


check_robot(robot1)
check_robot(robot2)