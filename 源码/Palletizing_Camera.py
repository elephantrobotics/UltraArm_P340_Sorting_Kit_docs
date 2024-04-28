import cv2 as cv
import numpy as np
import time

class Palletizing_Camera():
    def __init__(self,cap_num=1,pump_x=6,pump_y=11) -> None:
        """
        cap_num: 相机编号;
        pump_x: 吸盘在基坐标系X轴的补偿量;
        pump_y: 吸盘在基坐标系Y轴的补偿量;
        """
        # y轴偏移量
        self.pump_y =pump_y
        # x轴偏移量
        self.pump_x = pump_x   
        cap_num = cap_num
        self.cap = cv.VideoCapture(cap_num,cv.CAP_DSHOW)
        
        self.aruco_dict = cv.aruco.Dictionary_get(cv.aruco.DICT_6X6_250)
       
        self.aruco_params = cv.aruco.DetectorParameters_create()
         
        self.camera_matrix = np.array([
            [827.29511682, 0., 368.87666292],
            [0.,  824.88958537, 262.03016541],
            [0., 0., 1.]])

      
        self.dist_coeffs = np.array(([[0.21780081, -0.56324781, 0.01165061,   0.01845253,
             -1.0631406]]))
        
  
        
    
    def detect(self):
        try:
            print('start')
            num = 0
            start_time = time.time()
            while (time.time() - start_time) < 5 :
                success, img = self.cap.read()
                if not success:
                    print("It seems that the image cannot be acquired correctly.")
                    break
                cv.imshow("encode_image", img)
                gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)   
                corners, ids, rejectImaPoint = cv.aruco.detectMarkers(
                    gray, self.aruco_dict, parameters=self.aruco_params
                )

                if len(corners) > 0:
                    if ids is not None:
                        id=int(ids[0][0])
                        ret = cv.aruco.estimatePoseSingleMarkers(
                            corners, 0.022, self.camera_matrix, self.dist_coeffs
                        )
                        (rvec, tvec) = (ret[0], ret[1])
                        xyz = tvec[0, 0, :]
                        xyz = [round(xyz[0]*1000+self.pump_x, 2), round(xyz[1]*1000+self.pump_y, 2), round(xyz[2]*1000, 2)]
                        
                        try:
                            rvec = np.reshape(rvec, (3, 1))
                        except ValueError as e:
                            print("reshape错误：", e)
                            print("rvec1=",rvec)
                            rvec = np.array([[[-2.86279729, -0.00687534, -0.05316529]]])
                            # rvec=np.array([[[-2.86279729 -0.00687534 -0.05316529]]])
                            print("rvec2=",rvec)

                        rotation_matrix, _ = cv.Rodrigues(rvec)
                        
                        
                       
                        euler_angles = cv.RQDecomp3x3(rotation_matrix)[0]

                        yaw_angle = int(euler_angles[2])  
                       
                        if yaw_angle < -90:
                            yaw_angle = yaw_angle+90
                        elif yaw_angle > 90:
                            yaw_angle = yaw_angle-90
                        else:
                            yaw_angle = yaw_angle

                        yaw_angle-=38

                        
                        for i in range(rvec.shape[0]):
                            

                            cv.aruco.drawDetectedMarkers(img, corners,ids)
                        
                            if num < 100 :
                                num += 1
                            elif num ==100 :
                                cv.destroyAllWindows()                           
                                print("final_x:",xyz[0])
                                print("final_y:",xyz[1])
                                print("final_yaw_angle=",-yaw_angle)
                                return xyz[0],xyz[1],-yaw_angle,id
                cv.imshow("encode_image", img)
                cv.waitKey(1)

            raise Exception("未识别到Aruco二维码")
        finally:
            
            cv.destroyAllWindows()            


    def exception_handling(self):
        
        pass

    
    