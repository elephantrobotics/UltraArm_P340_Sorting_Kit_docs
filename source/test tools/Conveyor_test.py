import sys
import os
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) 
sys.path.append(BASE_DIR) 
from ConveyorMain import *
conveyer=ConveyorMain("COM13")

for i in range(2):
     conveyer.open_conveyor(100)
     time.sleep(3)
     conveyer.close_conveyor()
     time.sleep(2)
