import matplotlib.pyplot as plt
import numpy as np 
fig = plt.figure(figsize=(6, 4))
ax1 = fig.add_subplot(111)
x = np.linspace(-3 * np.pi, 3 * np.pi, 100)
y = np.sin(x)
plt.rcParams['font.sans-serif']=['SimHei'] 
plt.rcParams['axes.unicode_minus']=False 
plt.title(r'$f(x)=sin x$') 
ax1.spines['right'].set_color('none')
ax1.spines['top'].set_color('none')
ax1.xaxis.set_ticks_position('bottom')
ax1.spines['bottom'].set_position(('data', 0))
ax1.yaxis.set_ticks_position('left')
ax1.spines['left'].set_position(('data',0))
plt.plot(x, y)
plt.show()

