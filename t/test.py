# y = 8.5 * (x - 1365) - 403
# y = 5 * (x - 1464) - 332
import matplotlib.pyplot as plt
import numpy as np
x = np.linspace(1000, 3000, 10000)
y1 = (lambda x:8.5 * (x - 1365) - 403)(x)
y2 = (lambda x:5 * (x - 1464) - 332)(x)

plt.plot(x,y1,'r-')
plt.plot(x,y2,'b-')

plt.show()