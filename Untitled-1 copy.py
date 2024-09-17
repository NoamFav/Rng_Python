import matplotlib.pyplot as plt
from matplotlib.widgets import Slider

def collatz(n, tree, path):
    if n in tree:
        i = tree.index(n)
        path.extend(tree[i:])
        return path
    tree.append(n)
    if n == 1:
        return path
    if n % 2 == 0:
        return collatz(n // 2, tree, path)
    else:
        return collatz(3 * n + 1, tree, path)

tree = []
paths = []
for i in range(1, 101):
    path = []
    collatz(i, tree, path)
    paths.append(path)

fig, ax = plt.subplots()
plt.subplots_adjust(bottom=0.25)

num = 0

def update(val):
    global num
    num = int(snum.val)
    ax.clear()
    for path in paths:
        if num in path:
            ax.plot(range(len(path)), path, 'o-', markersize=4, c='red')
            for j, p in enumerate(path):
                ax.text(j, p, p, ha='center', va='center', fontsize=12)
        else:
            ax.plot(range(len(path)), path, 'o-', markersize=4, c='gray', alpha=0.2)
    ax.set_ylabel('Integer')
    ax.set_xlabel('Steps')
    ax.set_title('Collatz Conjecture')
    fig.canvas.draw_idle()

axcolor = 'lightgoldenrodyellow'
axnum = plt.axes([0.25, 0.1, 0.65, 0.03], facecolor=axcolor)
snum = Slider(axnum, 'Number', 1, 100, valinit=1, valstep=1)
snum.on_changed(update)

plt.show()
