import numpy as np
import matplotlib.pyplot as plt
plt.rcParams['font.sans-serif']=['SimHei'] 
plt.rcParams['axes.unicode_minus']=False 
fig = plt.figure(figsize=(4, 4))
ax = fig.add_subplot(111)
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')
ax.spines['bottom'].set_position(('data', 0))
ax.spines['left'].set_position(('data',0))
def u(t):
      r=np.where(t>=0.0,1.0,0.0)
      return r
t=np.arange(0,15)
plt.ylim(-1,3)
plt.stem(t,u(t))
plt.title(r'单位阶跃') 
plt.show()