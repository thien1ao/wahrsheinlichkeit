N_ROLLS = 3
OUTCOMES = 6


def _factor(n):
    if n == 1 or n == 0:
        return 1
    else:
        return _factor(n-1) * n


def _pow(n, p):
    res = 1
    for i in range(p):
        res *= n
    return res


def binom(n, k):
    return _factor(n) / (_factor(k) * _factor(n - k))


total = _pow(OUTCOMES, N_ROLLS)

binom_res = binom(OUTCOMES, N_ROLLS)

wahrscheinlichkeit = binom_res / total

print("wahrscheinlichkeit: %.4f" % wahrscheinlichkeit)
