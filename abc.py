import numpy as np
from matplotlib import pyplot
a = np.zeros((48, 48))
count = 0
cur = 1
block = 0
for x, y in np.ndindex(a.shape):
    if (count == 12):
        count = 0
        if x % 12 == 0:
            block += 1
        if block % 4 != 0:
            cur = (cur + 1) % 2
    a[x,y] = cur
    count += 1
print (a)
np.save("base", a)

pyplot.imshow(a, cmap=pyplot.cm.gray)
pyplot.show()
