import math
from operator import attrgetter
from random import random
import matplotlib.pyplot as plt

from Particle import Particle


def calculate_value_f(p):
    x1, x2, x3, x4 = p.vector_X
    f_value = 0.6224 * x1 * x3 * x4 + 1.7781 * x2 * x3 ** 2 + 3.1661 * x1 ** 2 * x4 + 19.84 * x1 ** 2 * x3
    if 0.0193 * x3 - x1 > 0 or 0.00954 * x3 - x2 > 0 \
            or -math.pi * x3 ** 2 * x4 - 4 / 3 * math.pi * x3 ** 3 + 129600 > 0 or -x4 - 240 > 0:
        return f_value * 10000
    else:
        return f_value


def update_values(p, leader):
    w, c1, c2 = (0.5 * random()) / 2.0, 1.5 * random(), 1.5 * random()
    v, x, p, pL = p.vector_V, p.vector_X, p.vector_P, leader.vector_P
    for i in range(4):
        v[i] = w * v[i] + c1 * (p[i] - x[i]) + c2 * (pL[i] - x[i])
        x[i] += v[i]


def main():
    particle_no = 30
    iter_no = 10000
    leader_values = []
    particles = [Particle() for i in range(particle_no)]
    for i in range(iter_no):
        for p in particles:
            temp_val = calculate_value_f(p)
            if p.f_value is None:
                p.f_value = temp_val
            if temp_val < p.f_value:
                p.f_value = temp_val
                p.vector_P = p.vector_X
        leader = min(particles, key=attrgetter('f_value'))
        leader_values.append(leader.f_value)
        for p in particles:
            update_values(p, leader)
    plt.plot(leader_values)
    plt.show()


if __name__ == "__main__":
    main()
