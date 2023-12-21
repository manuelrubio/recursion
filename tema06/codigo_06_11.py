__copyright__ = "Copyright (C) 2023 Manuel Rubio Sánchez"
__license__ = "MIT License"

def dibuja_L1(x, y):
    plt.plot([x, x + 2], [y + 2, y + 2], 'k-')
    plt.plot([x, x + 1], [y + 1, y + 1], 'k-')
    plt.plot([x + 1, x + 2], [y, y], 'k-')
    plt.plot([x, x], [y + 1, y + 2], 'k-')
    plt.plot([x + 1, x + 1], [y, y + 1], 'k-')
    plt.plot([x + 2, x + 2], [y, y + 2], 'k-')


def dibuja_L2(x, y):
    plt.plot([x, x + 2], [y + 2, y + 2], 'k-')
    plt.plot([x, x + 1], [y, y], 'k-')
    plt.plot([x + 1, x + 2], [y + 1, y + 1], 'k-')
    plt.plot([x, x], [y, y + 2], 'k-')
    plt.plot([x + 1, x + 1], [y, y + 1], 'k-')
    plt.plot([x + 2, x + 2], [y + 1, y + 2], 'k-')


def dibuja_L3(x, y):
    plt.plot([x, x + 2], [y, y], 'k-')
    plt.plot([x, x + 1], [y + 1, y + 1], 'k-')
    plt.plot([x + 1, x + 2], [y + 2, y + 2], 'k-')
    plt.plot([x, x], [y, y + 1], 'k-')
    plt.plot([x + 1, x + 1], [y + 1, y + 2], 'k-')
    plt.plot([x + 2, x + 2], [y, y + 2], 'k-')


def dibuja_L4(x, y):
    plt.plot([x, x + 2], [y, y], 'k-')
    plt.plot([x, x + 1], [y + 2, y + 2], 'k-')
    plt.plot([x + 1, x + 2], [y + 1, y + 1], 'k-')
    plt.plot([x, x], [y, y + 2], 'k-')
    plt.plot([x + 1, x + 1], [y + 1, y + 2], 'k-')
    plt.plot([x + 2, x + 2], [y, y + 1], 'k-')
