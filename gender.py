import numpy as np
import random

N = 1000
U_M = 170
O_M = 9
U_W = 160
O_W = 8
SIMULATIONEN = 10000


männer = np.random.normal(U_M, O_M, N)
frauen = np.random.normal(U_W, O_W, N)

mann_list = []
frau_list = []


def __iter__():
    frau_count = 0
    for i in range(SIMULATIONEN):
        mann = random.choice(männer)
        frau = random.choice(frauen)

        if (frau > mann):
            frau_count += 1

    print(f"Wahrscheinlichkeit: {frau_count / SIMULATIONEN:.2f}")


__iter__()












