import numpy as np
import matplotlib.pyplot as plt


def gradient(x1,x2):
    return np.array([4*(x1**3) + 2*x1 - x2 + 1,4*x2  - x1 + 2*x2 - 2])

def hessian(x1,x2):
    return np.array([[12*(x1**2)+2,-1],[-1,12*(x2**2)+2]])

xk = np.array([0,0])
x = []
y = []
x.append(xk[0])
y.append(xk[1])

for i in range(1,6):
    pk = np.dot( np.negative(np.linalg.inv(hessian(xk[0], xk[1]))), gradient(xk[0], xk[1]))
    xk = xk + pk
    x.append(xk[0])
    y.append(xk[1])
    print(xk)


fig = plt.figure()
ax = fig.add_subplot(111)

plt.plot(x,y)
i = 0
for xy in zip(x, y):
    ax.annotate('(x%s)' % i,xy=xy, textcoords='data')
    i = i + 1

plt.grid()
plt.show()