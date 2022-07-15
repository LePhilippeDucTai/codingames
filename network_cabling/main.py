import numpy as np


def read_coords():
    with open("input.txt") as f:
        n = int(f.readline())
        coords = [[int(j) for j in f.readline().split()] for _ in range(n)]
    return coords


def loss(y):
    return np.sum(np.abs(y))


def main():
    coords = read_coords()
    x_axis, y_axis = list(zip(*coords))
    y = np.array(sorted(y_axis), dtype=int)
    longueur_y = loss(y - np.median(y))
    longueur_x = max(x_axis) - min(x_axis)
    result = int(longueur_y + longueur_x)
    print(result)


if __name__ == "__main__":
    main()
