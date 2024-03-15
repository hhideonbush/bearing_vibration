from matplotlib.collections import PolyCollection
import matplotlib.pyplot as plt
from matplotlib import colors as mcolors
import numpy as np

axes=plt.axes(projection="3d")

def colors(arg):
    return mcolors.to_rgba(arg, alpha=0.6)


verts = []
z1 = [1, 2, 3, 4]
x1 = np.arange(0, 10, 0.4)
for z in z1:
    y1 = np.random.rand(len(x1))
    y1[0], y1[-1] = 0, 0
    verts.append(list(zip(x1, y1)))
# print(verts)
poly = PolyCollection(verts, facecolors=[colors('r'), colors('g'), colors('b'),
                                         colors('y')])
poly.set_alpha(0.7)
axes.add_collection3d(poly, zs=z1, zdir='y')

axes.set_xlabel('Time')
axes.set_xlim3d(0, 10)
axes.set_ylabel('Frequency')
axes.set_ylim3d(-1, 4)
axes.set_zlabel('Mag')
axes.set_zlim3d(0, 1)
axes.set_title("3D Waterfall plot")

plt.show()
