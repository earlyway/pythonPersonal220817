# https://stella47.tistory.com/138

#%matplotlib tk
import numpy as np
from scipy import interpolate

import matplotlib.pyplot as plt

plist = [(3 , 1), (2.5, 4), (0, 1),
        (-2.5, 4),(-3, 0), (-2.5, -4),
        (0, -1), (2.5, -4), (3, -1),]
ctr =np.array(plist)

x=ctr[:,0]
y=ctr[:,1]

plt.close()
l=len(x)

Order = 2

t=np.linspace(0,1,l-(Order-1),endpoint=True)
t=np.append(np.zeros(Order),t)
t=np.append(t,np.zeros(Order)+1)

tck=[t,[x,y],Order]
u3=np.linspace(0,1,(max(l*2,70)),endpoint=True)
out = interpolate.splev(u3,tck)

plt.plot(x,y,'k--',label='Control polygon',marker='o',markerfacecolor='red')
plt.plot(out[0],out[1],'b',linewidth=2.0,label='B-spline curve')
plt.legend(loc='best')
plt.axis([min(x)-1, max(x)+1, min(y)-1, max(y)+1])
plt.title('Cubic B-spline curve evaluation')
plt.show()