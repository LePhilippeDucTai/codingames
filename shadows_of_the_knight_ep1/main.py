import math

import numpy as np


def read_initial_config():
    with open("input.txt") as f:
        w, h = [int(x) for x in f.readline().split()]
        n = int(f.readline())
        x0, y0 = [int(x) for x in f.readline().split()]
        return w, h, n, x0, y0


def add(x, x0, lim):
    return min(max(0, x + x0), lim)


def reposition(dir, x0, y0, w, h):
    if dir == "UR":
        pos_x = (w + x0) // 2
        pos_y = add(y0, -1, h)
    elif dir == "DR":
        pos_x = (w + x0) // 2
        pos_y = add(y0, 1, h)
    elif dir == "UL":
        pos_x = x0 // 2
        pos_y = add(y0, -1, h)
    elif dir == "DL":
        pos_x = x0 // 2
        pos_y = add(y0, 1, h)
    elif dir == "U":
        pos_x = x0
        pos_y = y0 // 2
    elif dir == "D":
        pos_x = x0
        pos_y = (h + y0) // 2
    elif dir == "L":
        pos_x = x0 // 2
        pos_y = y0
    else:
        pos_x = (w + x0) // 2
        pos_y = y0
    return pos_x, pos_y


def main():
    w, h, n, x0, y0 = read_initial_config()
    bounds_x = (0, w)
    bounds_y = (0, h)

    bomb_dir = "UR"
    x, y = reposition(bomb_dir, x0, y0, bounds_x, bounds_y)
    x, y = reposition("R", x, y, w, h)
    x, y = reposition("L", x, y, w, h)
    print(x, y)


if __name__ == "__main__":
    main()
