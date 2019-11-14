import sys
import numpy as np
import argparse
from matplotlib import pyplot
from scipy.cluster.vq import vq, kmeans, whiten, kmeans2

parser = argparse.ArgumentParser(description='Get Dimension')
parser.add_argument('--dim', nargs=2, type = int)
args = parser.parse_args()
print (args.dim)
np.set_printoptions(threshold=sys.maxsize)
data = []
with open("output.txt") as f :
    data = f.read()

data = np.asarray(data.split(',')).astype(np.float)

whitened = whiten(data)
print (len(whitened))
bin = kmeans2(whitened,2)[1].reshape(args.dim[0], args.dim[1])
print(bin)
pyplot.imshow(bin, cmap=pyplot.cm.gray)
pyplot.show()
