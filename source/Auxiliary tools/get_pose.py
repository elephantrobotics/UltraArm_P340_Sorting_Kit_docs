from pymycobot.ultraArm import ultraArm
import time
ua = ultraArm("COM8", 115200)
# Obtain the current coordinates of the robot
coords = ua.get_coords_info()
print("coords",coords)
# Obtain robot joint angles
angel=ua.get_angles_info()
print("angel",angel)

