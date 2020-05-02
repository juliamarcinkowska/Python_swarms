import copy
import math
from operator import attrgetter
from random import random
import matplotlib.pyplot as plt

from Particle import Particle


def check_constraints(p):
    x1, x2, x3, x4 = p.vector_X
    if 0.0193 * x3 - x1 <= 0 and 0.00954 * x3 - x2 <= 0 \
            and -math.pi * x3 ** 2 * x4 - 4 / 3 * math.pi * x3 ** 3 + 1296000 <= 0 \
            and -x4 - 240 <= 0 and 1 <= x1 <= 99 and 1 <= x2 <= 99 and 10.00 <= x3 <= 200.00 and 10.00 <= x4 <= 200.00:
        return True
    else:
        return False


def euclidean_distance(particles, p):
    x1, x2, x3, x4 = p.vector_X
    for i in particles:
        x1p, x2p, x3p, x4p = i.vector_X
        dist = math.sqrt((x1 - x1p) ** 2 + (x2 - x2p) ** 2 + (x3 - x3p) ** 2 + (x4 - x4p) ** 2)


def calculate_value_f(p):
    p.vector_X[0] = int(p.vector_X[0])
    p.vector_X[1] = int(p.vector_X[1])
    x1, x2, x3, x4 = p.vector_X
    # print(x1, x2, x3, x4)
    f_value = 0.6224 * x1 * x3 * x4 + 1.7781 * x2 * x3 ** 2 + 3.1661 * x1 ** 2 * x4 + 19.84 * x1 ** 2 * x3
    if not check_constraints(p):
        return f_value + 10000000
    else:
        return f_value


def update_values(part, leader):
    w, c1, c2 = (0.5 * random()) / 2.0, 1.5 * random(), 1.5 * random()
    v, x, p, pl = part.vector_V, part.vector_X, part.vector_P, leader.vector_P
    for i in range(4):
        v[i] = w * v[i] + c1 * (p[i] - x[i]) + c2 * (pl[i] - x[i])
        x[i] += v[i]


def main():
    particle_no = 30
    iter_no = 10000
    leader_values = []
    leader = None
    particles = [Particle() for i in range(particle_no)]
    for i in range(iter_no):
        for p in particles:
            temp_val = calculate_value_f(p)
            if p.f_value is None:
                p.f_value = temp_val
            if temp_val < p.f_value:
                p.f_value = temp_val
                p.vector_P = p.vector_X.copy()
        leaders = sorted(particles, key=attrgetter('f_value'))
        for ld in leaders:
            if check_constraints(ld):
                leader = copy.deepcopy(ld)
                break
        leader_values.append(leader.f_value)
        for p in particles:
            update_values(p, leader)
    plt.plot(leader_values)
    plt.show()
    leader = min(particles, key=attrgetter('f_value'))
    print(leader_values[-1], ' ', leader.vector_P)


if __name__ == "__main__":
    main()
