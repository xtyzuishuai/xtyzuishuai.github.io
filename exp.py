# -*- coding: UTF-8 -*-
#coding=utf-8

import matplotlib.pyplot as plt
import numpy as np 
fig = plt.figure(figsize=(6, 4))
ax1 = fig.add_subplot(111)
x = np.linspace(-3,3,100)
y = np.exp(x)
plt.rcParams['font.sans-serif']=['SimHei'] #加上这一句就能在图表中显示中文
plt.rcParams['axes.unicode_minus']=False #用来正常显示负号
plt.title(r'$f(x)=e^x$') 
ax1.spines['right'].set_color('none')
ax1.spines['top'].set_color('none')
ax1.xaxis.set_ticks_position('bottom')
ax1.spines['bottom'].set_position(('data', 0))
ax1.yaxis.set_ticks_position('left')
ax1.spines['left'].set_position(('data',0))
plt.plot(x, y)
plt.show()
