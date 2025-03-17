import random
import numpy as np

N = 200
U_M = 170
O_M = 9
U_W = 160
O_W = 8
ARR_SIZE = 100
RAND_FIRST_N = 10
MIN_KÖRPERGRÖSSE = 150
MAX_KÖRPERGRÖSSE = 200

"""
:param const int N  Anzahl der Studierende in Hörsall
:param const int U_M  Erwartungswert  Männer
:param const int O_M  Standartverteilung Männer
:param const int U_W Erwartungswert Frauen
:param const int O_W Standartverteilung Frauen
"""

norm_arr = []


for _ in range(ARR_SIZE // 2):
    norm_arr.append(('M', np.random.normal(U_M, O_M)))


for _ in range(ARR_SIZE // 2):
    norm_arr.append(('W', np.random.normal(U_W, O_W)))

#rand_10_arr = arr[:RAND_FIRST_N]

#print(rand_10_arr)

def compare():
    mann =  random.choice([i for i in norm_arr if i[0] == 'M'])
    frau = random.choice([i for i in norm_arr if i[0] == 'W'])

    print(f"Mann: {mann[1]:.2f}, Frau: {frau[1]:.2f}")

def calculate_p(norm_arr):
    count = 0

    for i in range(len(norm_arr) - 1):
        mann = norm_arr[i]
        frau = norm_arr[i + 1]

        if frau > mann:
            count += 1

    p = count / N

    #for _ in range(N):
    #    mann = np.random.normal(U_M, O_M)
    #    frau = np.random.normal(U_W, O_W)

    #    if frau > mann:
    #        count += 1

    # p = count / N

    print(f"p: {p:.2f}")

compare()
calculate_p(norm_arr)



