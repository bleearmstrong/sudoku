import numpy as np
import random
import math

class Grid:


    def __init__(self):
        self.y = self.new_grid()
        while not self.validate():
            self.y = self.new_grid()

        self.counter = 0


    def new_grid(self):

        y = np.zeros((9, 9))
        y[y == 0.0] = np.nan
        random_start = [(random.randint(0, 8), random.randint(0, 8)) for _ in range(100)]
        random_start = random.sample(set(random_start), 11)
        start_elements = list(range(1, 10)) + [5] + [7]

        for i, item in enumerate(random_start):
            y[item[0], item[1]] = start_elements[i]
        return y


    def validate(self):
        for row in range(self.y.shape[0]):
            x = self.y[row, :].copy()
            z = [w for w in x if not math.isnan(w)]
            if len(z) != len(set(z)):
                return False
        for col in range(self.y.shape[1]):
            x = self.y[:, col].copy()
            z = [w for w in x if not math.isnan(w)]
            if len(z) != len(set(z)):
                return False
        for i in range(3):
            for j in range(3):
                t = self.y[(3 * i):(3 * (i + 1)), (3 * j):(3 * (j + 1))].flatten()
                if len(t) != len(set(t)):
                    return False
        return True

    def solve(self):

        if np.count_nonzero(~np.isnan(self.y)) == 81 and self.validate():
            return True
        min_nan = np.argwhere(np.isnan(self.y))[0]
        for i in range(1, 10):
            self.y[min_nan[0], min_nan[1]] = i
            if self.validate() and self.solve():
                return True
            self.y[min_nan[0], min_nan[1]] = np.nan
        return False

    def display(self):
        print('--------------------------------')
        for j, row in enumerate(self.y):
            line = '|'
            for i, item in enumerate(row):
                line += ' {} '.format(int(item))
                if i !=0 and (i + 1) % 3 == 0:
                    line += '|'
            print(line)
            if j != 0 and (j + 1) % 3 == 0:
                print('--------------------------------')





x = Grid()

x.y
x.solve()
x.y
x.display()