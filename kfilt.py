import matplotlib.pyplot as plt
import numpy as np
import cv2
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
                dif = (est_pos-x)/1.25
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

class KalmanFilter:
    kf = cv2.KalmanFilter(4,2)
    kf.measurementMatrix = np.array([[1,0,0,0],[0,1,0,0]],np.float32)
    kf.transitionMatrix = np.array([[1,0,1,0],[0,1,0,1],[0,0,1,0],[0,0,0,1]],np.float32)

    def predict(self, coordx,coordy) :

        measured = np.array([[np.float32(coordx)],[np.float32(coordy)]])
        self.kf.correct(measured)
        predicted = self.kf.predict()
        x ,y = int(predicted[0]),int(predicted[1])
        return x,y
kf = KalmanFilter()
# def update(): 
        # if x == None:
        #     return self.predict(True)
        # else:
        #     if self.vel == None:
        #         if self.pos == None:
        #             self.pos = x
        #         else:
        #             self.vel = x-self.pos
        #     else:
        #         if self.n>1:
        #             est_pos = self.predict(False)
        #             dif = (est_pos-self.pos)/1.25
        #             self.vel = self.vel - dif
        #         else:
        #             est_pos = self.predict()
        #             dif = (est_pos-x)/1.25
        #             self.vel = self.vel - dif
        #     return self.predict()


pos = [2,4,6,16,26,36,46,47,48,44,40,36,32,34,38,44,54,66,80]
# posy = [1,0,0,0,0,0]
# fx = kfxter()
# fy = kfxter()
# pred = []
# predkf = []
# for loc in range(len(pos)):
#     fx.update(posx[loc])
#     fy.update(posy[loc])
#     pred.append((fx.predict(),fy.predict()))
#     pred.append(fx.predict())
#     predkf.append(kf.predict(pos[loc],0)[0])

# print(posx)
# print(pred)
# print(predkf)
# plt.plot(posx[1:])
# plt.plot(pred)
# plt.plot(predkf)
# plt.show()

f = kfilter()
# pos = [10,12,14,None,18]
pred = []
predkf = []
for x in pos:
    pred.append(f.update(x))
    predkf.append(kf.predict(x,0)[0])


plt.plot(pos[1:],label = "Data")
plt.plot(pred,label = "Modified KF")
plt.plot(predkf,label = "KF")
er = np.array(pos[1:])-np.array(pred[:len(pos)-1])
plt.axhline(y=0.5, color='b', linestyle='-')
plt.plot(er,label = "Error")
plt.ylabel('Position')
plt.xlabel('Frame')
plt.legend()
plt.show()

# print(sum(np.abs(er))/len(er))



class KalmanFilterM:
    def __init__(self):
        self.velocity = None
        self.position = None

    def update(self, position = [None,None,None]):
        if position is None:
            position = self.position
            return self.predict()
        else:
            if self.velocity is None:
                if self.position is not None:
                    self.velocity = position - self.position
                self.position = position
                return self.predict()
            else:
                estimated_position = self.predict()
                difference = (estimated_position - position) / 1.25
                self.velocity -= difference
                self.position = position
                return self.predict()

    def predict(self):
        if self.velocity is None:
            return 0
        else:
            self.position += self.velocity
            return self.position + self.velocity


k = KalmanFilterM()
pos = [[0,0,0,],[0,1,2],[0,2,4]]
for x in pos:
    ret = k.update(x)
    print(ret)
