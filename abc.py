import numpy as np
from matplotlib import pyplot
a = np.random.rand(48, 48)
for x, y in np.ndindex(a.shape):
    if (a[x,y] > 0.5):
        a[x,y] = 1
    else:
        a[x,y] = 0
print (a)
pyplot.imshow(a, cmap=pyplot.cm.gray)
pyplot.show()
