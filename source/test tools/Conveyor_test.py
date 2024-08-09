import sys
import os
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) 
sys.path.append(BASE_DIR) 
from ConveyorMain import *
conveyer=ConveyorMain("COM13")

for i in range(100):
     try:
          conveyer.open_conveyor(100)
          time.sleep(5)
          conveyer.close_conveyor()
          time.sleep(2)
     #Press and hold the CTRL and C keys simultaneously to stop the conveyor belt.
     except KeyboardInterrupt:
          conveyer.close_conveyor()
