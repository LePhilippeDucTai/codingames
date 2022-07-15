def read_initial_config():
    with open("input.txt") as f:
        w, h = [int(x) for x in f.readline().split()]
        n = int(f.readline())
        x0, y0 = [int(x) for x in f.readline().split()]
        return w, h, n, x0, y0


class Batman:
    def __init__(self, x0, y0, w, h):
        self.x0 = x0
        self.y0 = y0
        self.x_min = 0
        self.x_max = w
        self.y_min = 0
        self.y_max = h

    def update_boundaries(self, command):
        if "U" in command:
            self.y_max = self.y0 - 1
        if "D" in command:
            self.y_min = self.y0 + 1
        if "L" in command:
            self.x_max = self.x0 - 1
        if "R" in command:
            self.x_min = self.x0 + 1

    def move(self):
        self.x0 = (self.x_min + self.x_max) // 2
        self.y0 = (self.y_min + self.y_max) // 2
        print(self.x0, self.y0)


def main():
    w, h, _, x0, y0 = read_initial_config()
    bat = Batman(x0, y0, w, h)
    bomb_dir = "UR"
    bat.update_boundaries(bomb_dir)
    bat.move()
    bat.update_boundaries("DR")
    bat.move()
    bat.update_boundaries("DL")
    bat.move()


if __name__ == "__main__":
    main()
