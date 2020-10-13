import numpy as np
import matplotlib.pyplot as plt
plt.rcParams['font.sans-serif']=['SimHei'] 
plt.rcParams['axes.unicode_minus']=False 
fig = plt.figure(figsize=(6, 4))
a = fig.add_subplot(111)
def u(t):
      r=np.where(t>0.0,1.0,0.0)
      return r
t=np.linspace(-3.0,3.0,10000)
plt.ylim(-1,3)
plt.plot(t,u(t))
plt.title(r'单位阶跃信号') 
a.spines['right'].set_color('none')
a.spines['top'].set_color('none')
a.xaxis.set_ticks_position('bottom')
a.spines['bottom'].set_position(('data', 0))
a.yaxis.set_ticks_position('left')
a.spines['left'].set_position(('data',0))
plt.show()