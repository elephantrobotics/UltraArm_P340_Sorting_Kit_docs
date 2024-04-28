import cv2 as cv
import numpy as np
import time


class Unstacking_Camera():
    def __init__(self,cap_num=2,pump_x=14,pump_y=5) -> None:
        """
        cap_num: 相机编号;
        pump_x: 吸盘在基坐标系X轴的补偿量;
        pump_y: 吸盘在基坐标系Y轴的补偿量;
        """
        # y轴偏移量
        self.pump_y =pump_y
        # x轴偏移量
        self.pump_x = pump_x  
        # 相机编号
        cap_num = cap_num
        self.cap = cv.VideoCapture(cap_num)
        self.aruco_dict = cv.aruco.Dictionary_get(cv.aruco.DICT_6X6_250)
        self.aruco_params = cv.aruco.DetectorParameters_create()
        self.camera_matrix = np.array([
            [827.29511682, 0., 368.87666292],
            [0.,  824.88958537, 262.03016541],
            [0., 0., 1.]])
        self.dist_coeffs = np.array(([[0.21780081, -0.56324781, 0.01165061,   0.01845253,
             -1.0631406]]))
        
        self.count=0
        


    def detect(self):
        while cv.waitKey(1) < 0:
            success, img = self.cap.read()
            if not success:
                print("It seems that the image cannot be acquired correctly.")
                break
            gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
            corners, ids, rejectImaPoint = cv.aruco.detectMarkers(
                gray, self.aruco_dict, parameters=self.aruco_params
            )
            positions = []           
            if ids is not None:              
                for i in range(len(ids)):
                        id=int(ids[i][0])
                        rvec, tvec, _ = cv.aruco.estimatePoseSingleMarkers(corners[i], 0.022, self.camera_matrix, self.dist_coeffs)
                        position = tvec.flatten()
                        arr = np.insert(position, 0, id)
                        positions.append(arr)                    
                cv.aruco.drawDetectedMarkers(img, corners,ids)
                positions = np.array(positions)
                positions[0:, 1:] *= 1000
                np.set_printoptions(precision=0, suppress=True)
                print("positions:",positions)
                sorted_positions = positions[np.argsort(positions[:, 1])]          
                a_sorted_positions = sorted_positions[:3][ np.argsort(sorted_positions[:3][:, 2])]
                b_sorted_positions = sorted_positions[3:][ np.argsort(sorted_positions[3:][:, 2])]
                merged_positions = np.concatenate((a_sorted_positions, b_sorted_positions), axis=0)
                sorted_positions=merged_positions              
                sorted_positions=sorted_positions.astype(int)
                print("sorted_positions:",sorted_positions)
                self.count+=1
            cv.imshow('Frame', img)
            if self.count==41:
                self.data_list=sorted_positions.tolist()
                for sublist in self.data_list:
                    sublist[1] -= self.pump_y
                    sublist[2] += self.pump_x
                print("data_list=",self.data_list)
                cv.destroyAllWindows()
                               
                self.count=0
                return self.data_list
            
    def exception_handling(self):
        while cv.waitKey(1) < 0:
            success, img = self.cap.read()
            if not success:
                print("It seems that the image cannot be acquired correctly.")
                break
            gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
            corners, ids, rejectImaPoint = cv.aruco.detectMarkers(
                gray, self.aruco_dict, parameters=self.aruco_params
            )
            positions = []           
            if ids is not None:              
                for i in range(len(ids)):
                        id=int(ids[i][0])
                        rvec, tvec, _ = cv.aruco.estimatePoseSingleMarkers(corners[i], 0.022, self.camera_matrix, self.dist_coeffs)
                        position = tvec.flatten()
                        arr = np.insert(position, 0, id)
                        positions.append(arr)                    
                cv.aruco.drawDetectedMarkers(img, corners,ids)
                positions = np.array(positions)
                positions[0:, 1:] *= 1000
                np.set_printoptions(precision=0, suppress=True)
                print("positions:",positions)
                sorted_positions = positions[np.argsort(positions[:, 1])]          
                a_sorted_positions = sorted_positions[:3][ np.argsort(sorted_positions[:3][:, 2])]
                b_sorted_positions = sorted_positions[3:][ np.argsort(sorted_positions[3:][:, 2])]
                merged_positions = np.concatenate((a_sorted_positions, b_sorted_positions), axis=0)
                sorted_positions=merged_positions              
                sorted_positions=sorted_positions.astype(int)
                
                
                print("sorted_positions:",sorted_positions)
                self.count+=1
            cv.imshow('Frame', img)
            if self.count==41:
                self.data_list=sorted_positions.tolist()
                if 315<self.data_list[0][3]<350 and 300<self.data_list[-1][3]<315:
                    self.data_list = [arr for arr in self.data_list if arr[3] <= 315]
                elif 365<self.data_list[0][3]<385 and 315<self.data_list[-1][3]<354:
                    self.data_list = [arr for arr in self.data_list if arr[3] <= 350]
                for sublist in self.data_list:
                    sublist[1] -= self.pump_y
                    sublist[2] += self.pump_x
                print("data_list=",self.data_list)
                cv.destroyAllWindows()
                               
                self.count=0
                return self.data_list
        
        
            
  