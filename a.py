import matplotlib.pyplot as plt
import numpy as np 
fig = plt.figure(figsize=(6, 4))
a = fig.add_subplot(111)
x = np.linspace(-3 * np.pi, 3 * np.pi, 100)
y = np.sin(x)
plt.rcParams['font.sans-serif']=['SimHei'] 
plt.rcParams['axes.unicode_minus']=False 
plt.title(r'$f(x)=sin x$') 
a.spines['right'].set_color('none')
a.spines['top'].set_color('none')
a.xaxis.set_ticks_position('bottom')
a.spines['bottom'].set_position(('data', 0))
a.yaxis.set_ticks_position('left')
a.spines['left'].set_position(('data',0))
plt.plot(x, y)
plt.show()

