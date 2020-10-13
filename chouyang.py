import numpy as np
import matplotlib.pyplot as plt
plt.rcParams['font.sans-serif']=['SimHei'] 
plt.rcParams['axes.unicode_minus']=False 
fig = plt.figure(figsize=(6, 4))
a = fig.add_subplot(111)
t = np.linspace(-5.0 * np.pi,5.0*np.pi,1000) 
y = np.sinc(t/np.pi) 
plt.ylim(-1,2)      
plt.rcParams['font.sans-serif']=['SimHei'] 
plt.rcParams['axes.unicode_minus']=False 
plt.title(r'$f(x)=e^x$') 
a.spines['right'].set_color('none')
a.spines['top'].set_color('none')
a.xaxis.set_ticks_position('bottom')
a.spines['bottom'].set_position(('data', 0))
a.yaxis.set_ticks_position('left')
a.spines['left'].set_position(('data',0))
plt.plot(t,y)              
plt.title(r'抽样信号') 
plt.show()  