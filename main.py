import numpy as np
import random
import math

class Grid:

    def __init__(self):
        self.y = self.new_grid()
        while not self.validate():
            self.y = self.new_grid()


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
        return True


x = Grid()

x.y