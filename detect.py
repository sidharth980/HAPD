import numpy as np
import matplotlib.pyplot as plt
import os
import cv2
from PIL import Image
import imutils

loc = r"C:\Users\Sidharth\Documents\code\HAPD\datasets\Carrada"
cam = r"camera_images"
ra = r"range_angle_numpy"
ad = "angle_doppler_processed"
rd = r"range_doppler_numpy"

def alight(num,loc):
    frame = "".join(["0" for _ in range(6-len(str(num)))])+str(num)
    return frame

def find_max_value1d(array):
    max_value = float('-inf')
    max_position = None

    for i, value in enumerate(array):
        if value > max_value:
            max_value = value
            max_position = i

    return max_value, max_position
def find_max_value_first_column(array):
    first_column = array[:, 0]  # Extract the first column
    max_value = np.max(first_column)  # Find the maximum value
    max_position = np.argmax(first_column)  # Find the position of the maximum value

    return max_value, max_position

class kfilter:
    def __init__(self) -> None:
        self.vel = None
        self.n = 1
        self.pos = None

    def update(self,x = None):
        if x == None:
            return self.predict(self.n)
        else:
            if self.vel == None:
                if self.pos != None:
                    self.vel = x-self.pos
                self.pos = x
                return self.predict()
            else:
                est_pos = self.predict()
                dif = (est_pos-x)*.25
                self.vel = self.vel - dif
                self.pos = x
                return self.predict()

    def predict(self,pos = None):
        if self.vel==None:
            return 0
        if pos==None:
            self.n = 0
            return self.vel+self.pos
        else:
            self.pos = self.pos + self.vel
            return self.pos + self.vel
        
def combine_adjacent_values(lst):
    combined_values = []
    start = None
    for i in range(len(lst)):
        if start is None:
            start = lst[i]
        if i == len(lst) - 1 or lst[i+1] != lst[i] + 1:
            if start != lst[i]:
                combined_values.append((start, lst[i]))
            else:
                combined_values.append([start])
            start = None

    return combined_values

def find_maxima_positions(numbers, threshold):
    maxima_positions = []
    
    for i, num in enumerate(numbers):
        if num > threshold:
            maxima_positions.append(i)
    
    return combine_adjacent_values(maxima_positions)

def ac(x,y):return x

save = 0
kf = kfilter()
def pred(num,loc,object = 0):
    global save
    frame = alight(num,loc)
    camera = cv2.imread(os.path.join(loc,os.path.join(cam,frame+".jpg")))
    radar = np.load(os.path.join(loc,os.path.join(ra,frame+".npy")))
    doppler = np.rot90(np.rot90(np.array(np.load(os.path.join(loc,os.path.join(rd,frame+".npy"))))))
    # plt.plot(np.sum(doppler,axis = 1))
    # plt.show()
    pos = []
    for x in range(0,256,5):
        row_sum = np.sum(radar[:250,x:x+4], axis=1)
        pos.append(find_max_value1d(row_sum))
    # print(pos)
    val = find_max_value_first_column(np.array(pos))
    pos = []
    val = find_max_value1d(np.sum(doppler,axis = 1)[:250])
    # plt.plot(np.sum(doppler,axis = 1))
    # plt.show()
    temp = find_maxima_positions(np.sum(doppler,axis = 1)[:250],2500) 
    # print(temp)
    hog = cv2.HOGDescriptor()
    hog.setSVMDetector(cv2.HOGDescriptor_getDefaultPeopleDetector())
    x, y = 1, 1
    valuesx = []
    i = 0
    valuesy = []
    image = camera
    
    image = imutils.resize(image,width=min(400, image.shape[1]))
    # print(image.shape)
    (regions, _) = hog.detectMultiScale(image,
                                        winStride=(4,4),
                                        padding=(4, 4),)
                                        # scale=1.05)
    # print("output in HOG", regions)
    
    angle = 0
    for (x1, y1, w, h) in regions:
        print(f"Position = ({x1},{y1}) ",end= " ")
        cv2.rectangle(image, (x1, y1),
                        (x1 + w, y1 + h),
                        (0, 0, 255), 2)
        angle = int(x1*64/400)+1
        print(f"Angle pos = {angle*90/64-45}",end= " ")
        i = i+1
        # valuesx.append(((x-x1)/x1)*100)
        # valuesy.append(((y-y1)/y1)*100)
        # cv2.rectangle(image, (x, y),
        #                 (x + w, y + h),
        #                 (0, 255, 0), 2)  # green= predicted

    # Showing the output Image
    if np.size(regions):
        if object == 0:
            valc = row_sum[angle]
        # valc  = kf.update((pos[val[1]][1]+5)*50/256)
        # save = 50-(pos[val[1]][1]+5)*50/256
        # print("Distance = ",(pos[val[1]][1]+5)*50/256,"Estimated = ",valc)
            val = ac(val[1],valc)
            valc = 50-(val)*50/256
            print("Distance = ",valc," Estimation = ",kf.update(valc))
        else:
            if len(temp)!=0:
                valc = 50-(temp[-1][-1])*50/256
                print("Distance = ",50-(temp[-1][-1])*50/256," Estimation = ",kf.update(valc))
            # print(valc)
        # else:
        #     print(save)

    cv2.imshow("Image", image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    hog = cv2.HOGDescriptor()
    hog.setSVMDetector(cv2.HOGDescriptor_getDefaultPeopleDetector())



# date = "2020-02-28-12-12-16"
# for x in range(40,80):
#     pred(x,os.path.join(loc,date))

# pred(41,os.path.join(loc,date))

# date = "2020-02-28-12-13-54"
# for x in range(57,72): 
#     pred(x,os.path.join(loc,date))


# date = "2020-02-28-13-07-38"
# for x in range(150,170):
#     pred(x,os.path.join(loc,date))

# date = "2020-02-28-13-09-58"
# for x in range(76,111):
#     pred(x,os.path.join(loc,date),1)

date = "2020-02-28-12-17-57"
for x in range(200,245):
    pred(x,os.path.join(loc,date))