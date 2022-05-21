from integer import Integer
from numba import njit
from time import perf_counter as pc
import matplotlib.pyplot as plt
import numpy as np

def fib_pure_py(n):
    if n <= 1:
        return n
    else:
        return(fib_pure_py(n-1) + fib_pure_py(n-2))

@njit
def fib_numba_py(n):
    if n <= 1:
        return n
    else:
        return(fib_numba_py(n-1) + fib_numba_py(n-2))

n = range(30, 34)
xp = []
xn = []
xf = []
pp30 = []
np30 = []

# data
def main():
    for i in n:
        start = pc()
        fib_pure_py(i)
        end = pc()
        xp.append(end-start)

        start = pc()
        p = fib_numba_py(i)
        end = pc()
        xn.append(end-start)

        f = Integer(i)
        start = pc()
        f.fib()
        end = pc()
        xf.append(end-start)

    for i in range(31):
        start = pc()
        fib_pure_py(i)
        end = pc()
        pp30.append(end-start)

        start = pc()
        fib_numba_py(i)
        end = pc()
        np30.append(end-start)
    print('.png saved')

    print(f'Times for python 1-30, {pp30}')
    print()
    print(f'Times for numba 1-30, {np30}')
    print()

    start = pc()
    fib_numba_py(30)
    end = pc()
    print(f'Time for numba 47, {end-start}')
    print()

    f = Integer(30)
    start = pc()
    f.fib()
    end = pc()
    print(f'Time for C++ 47, {end-start}')

    #plot
    fig, ax = plt.subplots()
    plt.scatter(n, xp, c='Green')
    plt.scatter(n, xn, c='Blue')
    plt.scatter(n, xf, c='Red')
    plt.savefig('FibTimes')

if __name__ == '__main__':
        main()
