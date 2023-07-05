import numpy as np
import os
import matplotlib.pyplot as plt
import kfilt as kf

class radar_range:

    def __init__(self) -> None:
        self.num = 0
        self.loc = r"C:\Users\Sidharth\Documents\code\HAPD\datasets\Carrada\2019-09-16-12-52-12"
        self.cam = r"camera_images"
        self.ra = r"range_angle_numpy"
        self.rd = r"range_doppler_numpy"
        self.ad = "angle_doppler_processed"
        self.prev = 0
        

    def find_range(self):
        normalized = 0
        self.frame = "".join(["0" for _ in range(6-len(str(self.num)))])+str(self.num)
        # self.radar = np.load(os.path.join(self.loc,os.path.join(self.ra,self.frame+".npy")))
        doppler = np.rot90(np.rot90(np.array(np.load(os.path.join(self.loc,os.path.join(self.rd,self.frame+".npy"))))))
        angle = np.rot90(np.rot90(np.array(np.load(os.path.join(self.loc,os.path.join(self.ad,self.frame+".npy"))))))
        angle = np.transpose(angle)
        fft_ra = np.dot(doppler,angle).mean(axis = 1)
        if self.num>1:
            prod = np.prod([fft_ra,self.prev],axis = 0)
            normalized = (256-np.unravel_index(np.argmax(prod), prod.shape)[0])*50/256
        self.prev = fft_ra
        self.num+=1
        return max((256-np.unravel_index(np.argmax(fft_ra), fft_ra.shape)[0])*50/256,normalized)

    def find_range_fft(self):
        self.frame = "".join(["0" for _ in range(6-len(str(self.num)))])+str(self.num)
        doppler = np.array(np.load(os.path.join(self.loc,os.path.join(self.rd,self.frame+".npy"))))
        fft_doppler = np.fft.fft(doppler).max(axis = 1).real
        self.num+=1
        cal = np.unravel_index(np.argmax(fft_doppler), fft_doppler.shape)[0]*50/256
        if cal > 10 and cal<19:
            return cal
        elif cal>20:
            return cal
        else: 
            return None
        



ra = radar_range()
kalm = kf.kfilter()
pos = []
ret = []
for x in range(0,250):
    ran = ra.find_range_fft()
    kran = kalm.update(ran)
    # kran = 0 if kran<0 or kran>50 else kran
    ret.append(0 if ran==None else ran)
    pos.append(kran)
    print(f"Range at Frame {x} = {ran} -> {kran}")
plt.plot(pos)
print(ret)
plt.plot(ret)
plt.ylabel("Distance (m)")
plt.xlabel("Frame")
plt.show()

