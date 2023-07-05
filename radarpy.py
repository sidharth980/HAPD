import numpy as np
import matplotlib.pyplot as plt
import os
import sys

# loc = r"C:\Users\Sidharth\Documents\code\HAPD\datasets\Carrada\2019-09-16-12-52-12"
# cam = r"camera_images"
# ra = r"range_angle_numpy"
# rd = r"range_doppler_numpy"
# ad = "angle_doppler_processed"

# num = 180
# frame = "".join(["0" for _ in range(6-len(str(num)))])+str(num)


# radar = np.load(os.path.join(loc,os.path.join(ra,frame+".npy")))
# doppler = np.rot90(np.rot90(np.array(np.load(os.path.join(loc,os.path.join(rd,frame+".npy"))))))
# angle = np.rot90(np.rot90(np.array(np.load(os.path.join(loc,os.path.join(ad,frame+".npy"))))))

# rad = radar[5:225,]
# plt.imshow(rad,cmap="magma")
# radar = radar[5:255,]
# pos = []
# for x in range(0,256,5):
#     ang = np.fft.fft(radar[:,x:x+5]).real
#     plt.plot(ang)
#     plt.show()
#     if np.amax(ang) > 20000:
#         pos.append([np.unravel_index(np.argmax(ang), ang.shape)[0],x])

# plt.plot(np.fft.fft(radar[:,96:98]))
# plt.show()


import numpy as np

# Load CSV file into numpy array
csv_file = 'data.csv'  # Replace with the name of your CSV file
data = np.loadtxt(csv_file, delimiter=',')  # Assumes the CSV file has comma as delimiter

radar = data[5:226]
for x in range(2):
    resl = np.fft.fft(radar[:,x:x+6]).real
    for l in range(len(resl)):
        print(f"{l}: {resl[l][0]}")

