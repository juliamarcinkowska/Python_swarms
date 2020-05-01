import random
import math

import numpy as np


class Particle:
    def __init__(self):
        x1, x2, x3, x4 = np.array([random.randint(1, 99), random.randint(1, 99),
                  random.uniform(10.0, 200.0), random.uniform(10.0, 200.0)])
        while 0.0193 * x3 - x1 > 0 or 0.00954 * x3 - x2 > 0 \
                or -math.pi * x3 ** 2 * x4 - 4 / 3 * math.pi * x3 ** 3 + 129600 > 0 or -x4 - 240 > 0:
            x1 = random.randint(1, 99)
            x2 = random.randint(1, 99)
            x3 = random.uniform(10.0, 200.0)
            x4 = random.uniform(10.0, 200.0)
        self.vector_X = np.array([x1, x2, x3, x4])
        self.vector_V = np.array([random.uniform(-50.0, 50.0), random.uniform(-50.0, 50.0),
                                  random.uniform(-95.0, 95.0), random.uniform(-95.0, 95.0)])
        self.vector_P = np.array([x1, x2, x3, x4])
        self.f_value = None
