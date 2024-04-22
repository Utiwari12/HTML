import matplotlib

print(matplotlib.__version__)
import matplotlib.pyplot as plt
import numpy as np
# xpoints=np.array([8,3,15])
# ypoints=np.array([5,7,20])
# plt.plot(xpoints,ypoints, 'o:k')
# plt.show()
x=np.array([60,65,70,80,90,100])
y=np.array([200,220,230,250,265,275])
plt.title("Sport Data")
plt.xlabel("Average pulsa")
plt.ylabel("Burning Calories")
plt.plot(x,y)
plt.grid()
plt.show()