from pymycobot.ultraArm import ultraArm
import time
ua = ultraArm("COM8", 115200)
# 获取机器人当前坐标
coords = ua.get_coords_info()
print("coords",coords)
# 获取机器人当前坐标
angel=ua.get_angles_info()
print("angel",angel)

