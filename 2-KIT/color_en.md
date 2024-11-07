# Color sorting case

**Case description**: This case will sort the red, green, blue and yellow wooden blocks to the specified location

## 1 Get the case program
[Source code download address](https://github.com/elephantrobotics/UltraArm_P340_Sorting_Kit_docs/tree/ultraarm_sorting_kit_gitbook-cn)

<img src="./img/4.png" width="50%" height="50%">

## 2 Threshold adjustment
**Note**: Under different lighting conditions, the threshold may be different. You can run the program first to see if it can be captured normally. If not, you need to adjust the color threshold that cannot be recognized by yourself

Run hsv. py file, a window will pop up. Use the slider to adjust the threshold. After adjusting to the appropriate threshold, a green box will appear to frame the wooden block. Then fill in the threshold in the corresponding file. 1_color_thresholds.txt corresponds to camera No. 1, and 2_color_thresholds.txt corresponds to camera No. 2.

The following takes the red wooden block as an example. The two cameras adjust the threshold of the red wooden block respectively, and fill the adjusted threshold in the corresponding file. The threshold adjustment of other colors is the same method.

<img src="./img/1.png" width="50%" height="50%">

<img src="./img/2.png" width="50%" height="50%">

## 3 Case Reproduction
According to the QR code case debugging method, determine the serial port number and camera number of each device and the hand-eye calibration parameters, fill them in color_demo.py, and then run the program.
If you are not sure, you can adjust the hand-eye calibration parameters appropriately.

<img src="./img/3.png" width="50%" height="50%">