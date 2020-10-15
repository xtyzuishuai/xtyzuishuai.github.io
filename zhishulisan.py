import numpy as np
import matplotlib.pyplot as plt
fig = plt.figure(figsize=(4, 4))
ax = fig.add_subplot(111)
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')
ax.spines['bottom'].set_position(('data', 0))
ax.spines['left'].set_position(('data',0))
n=np.arange(0,15)
a=3/4
f=a**n
plt.stem(n,f)
plt.title(u'y=(3/4)^x')
plt.xlabel('x')
plt.ylabel('y')
plt.show()

