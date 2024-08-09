import sys
import os
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) 
sys.path.append(BASE_DIR) 
from ConveyorMain import *
conveyer=ConveyorMain("COM5")

for i in range(100):
     try:
          conveyer.open_conveyor(100)
          time.sleep(5)
          conveyer.close_conveyor()
          time.sleep(2)
     #按住键盘CTRL+C键，可让传送带停止
     except KeyboardInterrupt:
          conveyer.close_conveyor()
