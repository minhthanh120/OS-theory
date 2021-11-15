import matplotlib.pyplot as plt
x = [1, 2, 3, 4]
y = [10, 20, 25, 30]
fig = plt.figure()
ax = fig.add_subplot(111)
ax.plot(x, y, color='lightblue', linewidth=3)
ax.scatter([2, 4, 6],
           [5, 15, 25],
           color='darkgreen',
           marker='^')
ax.set_xlim(1, 6.5)
plt.savefig('foo.png')
plt.show()
