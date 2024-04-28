import cv2
import cv2.aruco as aruco
import numpy as np

#Camera number
cam_num=2

cap = cv2.VideoCapture(cam_num)
cameraMatrix =np.array([
            [827.29511682, 0., 368.87666292],
            [0.,  824.88958537, 262.03016541],
            [0., 0., 1.]])


distCoeffs = np.array(([[0.21780081, -0.56324781, 0.01165061,   0.01845253,
             -1.0631406]]))








aruco_dict = aruco.Dictionary_get(aruco.DICT_6X6_250)
parameters = aruco.DetectorParameters_create()

while True:
    
    ret, frame = cap.read()
    
    
    corners, ids, rejected = aruco.detectMarkers(frame, aruco_dict, parameters=parameters)
    
    
   
    if len(corners) > 0:
        for i in range(len(ids)):
            
            print("二维码ID:", ids[i][0])
            
           
            rvec, tvec, _ = aruco.estimatePoseSingleMarkers(corners[i], 0.022, cameraMatrix, distCoeffs)
            
            
            xyz = tvec[0, 0, :]
           
            print("rvec=",rvec)
            
            xyz = [round(xyz[0]*1000, 2), round(xyz[1]*1000, 2), round(xyz[2]*1000, 2)]
            print("xyz is:",xyz)
            if rvec.shape == (3, 1):
                        
                    pass
            else:
                        
                    rvec = rvec.reshape((3, 1))
                    # rvec = rvec.reshape((3, 1))
            rotation_matrix, _ = cv2.Rodrigues(rvec)
                    
                    # 获取欧拉角
            euler_angles =  cv2.RQDecomp3x3(rotation_matrix)[0]
                    
                   
            yaw_angle = int(euler_angles[2])  
           
            print("yaw_angle:",-yaw_angle) 
    
        
        frame = aruco.drawDetectedMarkers(frame, corners, ids)
        
     
    
    cv2.imshow('ArUco', frame)
    
    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break


cap.release()
cv2.destroyAllWindows()
