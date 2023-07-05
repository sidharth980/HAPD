import numpy as np
import matplotlib.pyplot as plt
import os
import sys
from PIL import Image

# angle_doppler = np.load('200070.npy')
# range_angle = np.load('000070.npy')
# range_angle = np.load('000070.npy')
# range_doppler = np.load('400070.npy')
# range_doppler = np.load('300070.npy')
# # angle_doppler = np.load('500070.npy')

# # img = mpimg.imread('000070.jpg')
# img_pil = Image.open("000070.jpg")
# img_pil = img_pil.resize((256,256),Image.ANTIALIAS)
# img_bw = img_pil.convert('1')
# np_img = np.array(img_bw)
# print(len(range_doppler))

# range_doppler = np.array(range_doppler)
# rot = np.rot90(np.rot90(range_doppler))
# bol = rot>110
# img = bol.astype(int)
# print(bol.shape)
# pos = (256-np.unravel_index(np.argmax(bol), bol.shape)[0])*50/256
# # print(true_positions = np.argwhere(arr))
# print(pos)
# plt.imshow(img,cmap = 'magma')
# plt.colorbar()
# plt.show()
# plt.imshow(rot,cmap = 'magma')
# plt.colorbar()
# plt.show()

# plt.subplot(1,3,1)
# plt.imshow(range_angle,cmap = "magma")
# plt.subplot(1,3,2)
# print(np.argmax(range_doppler)/2)
# plt.imshow(np.rot90(np.rot90(range_doppler)),cmap = "magma")
# plt.subplot(1,3,3)
# plt.imshow(np.rot90(np.rot90(angle_doppler)),cmap = "magma")
# plt.show()

# datasets\Carrada\2020-02-28-13-15-36
# 2019-09-16-12-52-12
#DATASET LOCATION 
loc = r"C:\Users\Sidharth\Documents\code\HAPD\datasets\Carrada\2019-09-16-12-52-12"
cam = r"camera_images"
ra = r"range_angle_numpy"
rd = r"range_doppler_numpy"
ad = "angle_doppler_processed"
# num = sys.argv[1]
num = int(sys.argv[1])
delay = 2
frame = "".join(["0" for _ in range(6-len(str(num)))])+str(num)

#LOAD DATASET
camera = Image.open(os.path.join(loc,os.path.join(cam,frame+".jpg")))
radar = np.load(os.path.join(loc,os.path.join(ra,frame+".npy")))
doppler = np.rot90(np.rot90(np.array(np.load(os.path.join(loc,os.path.join(rd,frame+".npy"))))))
angle = np.rot90(np.rot90(np.array(np.load(os.path.join(loc,os.path.join(ad,frame+".npy"))))))

frame_prev = "".join(["0" for _ in range(6-len(str(num-delay)))])+str(num-delay)
radar_prev = np.load(os.path.join(loc,os.path.join(ra,frame_prev+".npy")))
doppler_prev = np.rot90(np.rot90(np.array(np.load(os.path.join(loc,os.path.join(rd,frame_prev+".npy"))))))
angle_prev = np.rot90(np.rot90(np.array(np.load(os.path.join(loc,os.path.join(ad,frame_prev+".npy"))))))

#CALCULATIONS
# peak_dop = doppler>50
# peak_dop = peak_dop.astype(int)
fft_rd = np.dot(radar,doppler)
angle = np.transpose(angle)
fft_ra = np.dot(doppler,angle)
fft_fft_rf = np.dot(radar,fft_ra)
fft_fft_rd = np.dot(fft_ra,doppler)

fft_rd_prev = np.dot(radar_prev,doppler_prev)
angle_prev = np.transpose(angle_prev)
fft_ra_prev = np.dot(doppler_prev,angle_prev)
fft_fft_rf_prev = np.dot(radar_prev,fft_ra_prev)
fft_fft_rd_prev = np.dot(fft_ra_prev,doppler_prev)


avg_ra = fft_ra.mean(axis = 1)
avg_rd = fft_fft_rd.mean(axis=1)
avg_ra_prev =fft_ra_prev.mean(axis = 1)
avg_rd_prev = fft_fft_rd_prev.mean(axis=1)

# dot_ra = np.prod([avg_ra,avg_ra_prev], axis=0)
# dot_rd = np.prod([avg_rd,avg_rd_prev], axis=0)
# print((256-np.unravel_index(np.argmax(fft_fft_rd), fft_fft_rd.shape)[0])*50/256)
# print((256-(np.unravel_index(np.argmax(dot_ra), dot_ra.shape)[0]))*50/256)
cor = np.convolve(avg_ra,avg_ra_prev)

#PLOT/VISUALIZATION
fg,ax = plt.subplots(5,4)
ax[0,0].imshow(radar,cmap="magma")
ax[0,1].imshow(doppler,cmap="magma")
ax[0,2].imshow(angle,cmap = "magma")
ax[0,3].imshow(camera)
ax[1,0].imshow(fft_rd,cmap="magma")
ax[1,1].imshow(fft_ra,cmap="magma")
ax[1,2].imshow(fft_fft_rf,cmap="magma")
ax[1,3].imshow(fft_fft_rd,cmap="magma")
ax[2,0].imshow(fft_rd_prev,cmap="magma")
ax[2,1].imshow(fft_ra_prev,cmap="magma")
ax[2,2].imshow(fft_fft_rf_prev,cmap="magma")
ax[2,3].imshow(fft_fft_rd_prev,cmap="magma")
ax[3,0].plot(avg_ra)
ax[3,1].plot(avg_rd)
ax[3,2].plot(avg_ra_prev)
ax[3,3].plot(avg_rd_prev)
ax[4,0].plot(cor)
# ax[4,1].plot(np.log10(dot_rd))

# ax[3,0].plot(np.correlate(np.log10(fft_ra.max(axis = 1)),np.log10(fft_ra_prev.max(axis = 1))))
# ax[2,1].imshow(np.log2(fft_next))
plt.show()


