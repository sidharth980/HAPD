import numpy as np
import matplotlib.pyplot as plt

# val0 = [1,2,3,4,5,6,7,8,9,10,11,12]
val1 = [0,.2,.9,.95,.95,.9,.84,.82,.78,.75,.72,.6,.4,.3,.25,.23,.2]
plt.plot(val1)
plt.xlabel("Distance (m)")
plt.ylabel("Accuracy")
plt.title("Accuracy Of HOG+SVM")
plt.show()