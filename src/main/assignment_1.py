import math
import numpy as np


def exact_value(ex: float, m: float):
    ex = ex - 1023
    ex = pow(2, ex)
    m = 1 + m
    exact = ex * m
    return exact


def round_chop(num: float, deci: int):
    fac = 10 ** deci
    return math.floor((num * fac) / fac) * .001


def round_up(r: float):
    fac = 10 ** 3
    return math.ceil(r * fac) / fac


def func(q: float):
    return (q * q * q) + (4 * (q * q)) - 10


def func_delta(l: float):
    return 3 * (l * l) + (8 * l)


def bisection_calc(a: float, b: float):
    tol = .0001
    max_iter_bi = 20
    iter_ct_bi = 0

    while iter_ct_bi <= max_iter_bi:

        mid = (a + b) / 2

        if abs(a - b) <= tol:
            return iter_ct_bi
        elif np.sign(func(a)) != np.sign(func(mid)):
            b = mid
        elif np.sign(func(b)) != np.sign(func(mid)):
            a = mid

        iter_ct_bi = iter_ct_bi + 1

    return iter_ct_bi


def func_nw(nw: float):
    tol = .0001
    new_nw = nw

    res = func(nw) / func_delta(nw)

    nw_ct = 1

    while abs(res) >= tol:
        new_nw = new_nw - res
        
        nw_ct = 1 + nw_ct
        
        res = func(new_nw) / func_delta(new_nw)

    return nw_ct


if __name__ == "__main__":
    x = float(0b10000000111)
    y = float(0b111010111001)

    y = math.frexp(y)

    (mantis, trash) = y
    ans = exact_value(x, mantis)

    i = "{0:.4f}".format(ans)
    j = round_chop(ans, 3)
    j = "{0:.3f}". format(j)
    k_ans = round_up(ans * .001)

    print(i, end="\n\n")
    print(j, end="\n\n")
    print(k_ans, end="\n\n")

    i = float(i)

    k = k_ans * 1000
    abs_round_error = abs(i - k) * .001
    print(abs_round_error)

    rel_round_error = abs(i - k)
    rel_round_error = rel_round_error / abs(i)
    print(rel_round_error, end="\n\n")

    n = pow(10, 1 / 3) * 10
    n = n - 1
    n = round(n)
    print(n, end="\n\n")

    bisection_ct = bisection_calc(-4, 7)
    print(bisection_ct, end="\n\n")

    newton_method = func_nw(7)
    print(newton_method)


