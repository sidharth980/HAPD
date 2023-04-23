import numpy as np
import pandas as pd
import os

def npm_to_csv(num,date):
    
    loc = os.path.join(os.getcwd(),"datasets\Carrada")
    # loc = r"C:\Users\Sidharth\Documents\code\HAPD\datasets\Carrada"
    cam = r"camera_images"
    ra = r"range_angle_numpy"
    rd = r"range_doppler_numpy"
    ad = "angle_doppler_processed"
    loc = os.path.join(loc,date)
    frame = "".join(["0" for _ in range(6-len(str(num)))])+str(num)

    # doppler = np.rot90(np.rot90(np.array(np.load(os.path.join(loc,os.path.join(rd,frame+".npy"))))))
    radar = np.load(os.path.join(loc,os.path.join(ra,frame+".npy")))
    # Convert the array to a Pandas dataframe
    df = pd.DataFrame(radar)
    # dff = pd.DataFrame(np.fft.fft(doppler).real)


    # Write the dataframe to a CSV file
    df.to_csv(f"csv/{num}.csv", index=False)
    # dff.to_csv('dataoutpy.csv',index=False)



date = "2019-09-16-12-52-12"
npm_to_csv(180,date)