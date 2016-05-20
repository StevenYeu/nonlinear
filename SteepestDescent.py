import numpy as np
import matplotlib.pyplot as plt

xk = np.array([1,1])
x = []
y = []
x.append(xk[0])
y.append(xk[1])
H = np.array([[2,-1],[-1,40]])
alpha = np.dot(xk,(np.dot(np.dot(H,H),xk)))/(np.dot(xk,np.dot(np.dot(H,np.dot(H,H)),xk)))


for k in range(1,21):
    x1 = xk[0] - (alpha * (2*xk[0] - xk[1]))
    x2 = xk[1] - (alpha * (-xk[0] + 40*xk[1]))
    xk = np.array([x1,x2])
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