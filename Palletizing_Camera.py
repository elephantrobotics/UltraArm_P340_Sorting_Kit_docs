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
        
        self.thresholds =self.read_thresholds_from_file('2_color_thresholds.txt')
        
  
        
    
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


    # 读取存储阈值的文本文件
    def read_thresholds_from_file(self,filename):
        thresholds = {}
        with open(filename, 'r') as file:
            lines = file.readlines()
            color = None
            
            for line in lines:
                line = line.strip()
                if not line:
                    continue
                
                if line.endswith(':'):
                    # 新颜色块开始
                    color = line[:-1]  # 去掉冒号
                    thresholds[color] = {}
                elif 'Low' in line or 'High' in line:
                    # 提取阈值
                    key, value = line.split(':')
                    key = key.strip()
                    value = int(value.strip())
                    thresholds[color][key] = value
        return thresholds
                                    
    def detect_color(self):
        data_list=[]
        lower_bound=[]
        upper_bound=[]
        detected_colors = None
        img=None
        while cv.waitKey(1) < 0:
            for i in range(10):
                success, img = self.cap.read()
            if not success:
                print("It seems that the image cannot be acquired correctly.")
                break
            marker_size=0.03
            for color, values in self.thresholds.items():
                lower_bound.append( np.array([values["Low H"], values["Low S"], values["Low V"]]))
                upper_bound.append(np.array([values["High H"], values["High S"], values["High V"]]))  

            img=img[30:310,180:420]
            hsv = cv.cvtColor(img, cv.COLOR_BGR2HSV)
                
            lower_red =  lower_bound[0]
            upper_red = upper_bound[0]
            lower_green = lower_bound[1]
            upper_green = upper_bound[1]
            lower_blue = lower_bound[2]
            upper_blue = upper_bound[2]
            lower_yellow = lower_bound[3]
            upper_yellow = upper_bound[3]
            
            red_mask = cv.inRange(hsv, lower_red, upper_red)
            blue_mask = cv.inRange(hsv, lower_blue, upper_blue)
            green_mask = cv.inRange(hsv, lower_green, upper_green)
            yellow_mask = cv.inRange(hsv, lower_yellow, upper_yellow)
        
           
            kernel = np.ones((5, 5), np.uint8)
            red_mask = cv.morphologyEx(red_mask, cv.MORPH_OPEN, kernel)
            blue_mask = cv.morphologyEx(blue_mask, cv.MORPH_OPEN, kernel)
            green_mask = cv.morphologyEx(green_mask, cv.MORPH_OPEN, kernel)
            yellow_mask = cv.morphologyEx(yellow_mask, cv.MORPH_OPEN, kernel)

            contours, _ = cv.findContours(red_mask + blue_mask + green_mask+ yellow_mask, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)
            for contour in contours:
                color = ""
                if cv.contourArea(contour) > 100:  
                    if np.any(red_mask):
                        color = "red"
                    elif np.any(blue_mask):
                        color = "blue"
                    elif np.any(green_mask):
                        color = "green"
                    elif np.any(yellow_mask):
                        color = "yellow"
                    detected_colors=color
                    rect = cv.minAreaRect(contour)
                    box = cv.boxPoints(rect)
                    box = np.int0(box)
                    restored_coordinates = []
                    for point in box:
                        restored_point = (point[0] + 180, point[1] + 30)  
                        restored_coordinates.append(restored_point)
                    corners = np.array([[restored_coordinates[0], restored_coordinates[1], restored_coordinates[2], restored_coordinates[3]]], dtype=np.float32)
                    rvec, tvec, _ = cv.aruco.estimatePoseSingleMarkers(corners, marker_size, self.camera_matrix,self.dist_coeffs)
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
                    cv.drawContours(img, [box], 0, (0, 0, 255), 2)
                    frame = cv.circle(img,  tuple(map(int, rect[0])), 5, (0, 0, 255), -1)
                    cv.putText(frame, detected_colors, (int(rect[0][0])-50, int(rect[0][1])),  cv.FONT_HERSHEY_SIMPLEX, 0.7, (255,255,255), 2)
                    cv.imshow('frame', frame)
                    
                    cv.waitKey(1500)
                    cv.destroyAllWindows()
                    for i in range(2):
                        data_list.append(round(tvec.flatten()[i]*1000,2))
                    data_list[0]+=self.pump_x
                    data_list[1] += self.pump_y
                    data_list.append(yaw_angle)
                    data_list.append(detected_colors)
                    # print("data_list=",data_list)
                    return data_list
            else:
                pass

    def exception_handling(self):
        
        pass

    
    