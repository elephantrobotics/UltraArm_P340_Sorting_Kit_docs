import cv2
import cv2.aruco as aruco
import numpy as np

#相机编号
cam_num=1

# 获取摄像头输入
cap = cv2.VideoCapture(cam_num)
cameraMatrix =np.array([
            [827.29511682, 0., 368.87666292],
            [0.,  824.88958537, 262.03016541],
            [0., 0., 1.]])

        # 摄像头的畸变系数
distCoeffs = np.array(([[0.21780081, -0.56324781, 0.01165061,   0.01845253,
             -1.0631406]]))



# 定义字典和参数
aruco_dict = aruco.Dictionary_get(aruco.DICT_6X6_250)
parameters = aruco.DetectorParameters_create()

while True:
    # 读取当前帧
    ret, frame = cap.read()
    
    # 检测ArUco二维码
    corners, ids, rejected = aruco.detectMarkers(frame, aruco_dict, parameters=parameters)
    
    
    # 打印检测到的二维码信息
    if len(corners) > 0:
        for i in range(len(ids)):
            
            print("二维码ID:", ids[i][0])
            
            # 估计位姿态
            rvec, tvec, _ = aruco.estimatePoseSingleMarkers(corners[i], 0.022, cameraMatrix, distCoeffs)
            
            
            xyz = tvec[0, 0, :]
           
            print("rvec=",rvec)
            
            xyz = [round(xyz[0]*1000, 2), round(xyz[1]*1000, 2), round(xyz[2]*1000, 2)]
            print("xyz is:",xyz)
            if rvec.shape == (3, 1):
                        # `rvec` 已正确解析为 3x1 的矩阵
                    pass
            else:
                        # `rvec` 没有正确解析为 3x1 的矩阵
                        # 可以尝试对 `rvec` 进行调整
                    rvec = rvec.reshape((3, 1))
                    # rvec = rvec.reshape((3, 1))
            rotation_matrix, _ = cv2.Rodrigues(rvec)
                    
                    # 获取欧拉角
            euler_angles =  cv2.RQDecomp3x3(rotation_matrix)[0]
                    
                    # 欧拉角包含了旋转角度，可以按需要选择适当的坐标轴和单位
                    # roll_angle = euler_angles[0]  # 绕X轴的旋转角度
                    # pitch_angle = euler_angles[1]  # 绕Y轴的旋转角度
            yaw_angle = int(euler_angles[2])  # 绕Z轴的旋转角度
            # print("Z_angles",yaw_angle)
            print("yaw_angle:",-yaw_angle) 
    
        # 在图像上绘制并显示ArUco二维码
        frame = aruco.drawDetectedMarkers(frame, corners, ids)
        
     
    
    cv2.imshow('ArUco', frame)
    
    # 按下'q'键退出循环
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# 释放摄像头并关闭窗口
cap.release()
cv2.destroyAllWindows()
