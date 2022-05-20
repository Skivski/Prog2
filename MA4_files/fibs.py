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

n = [20, 25, 28]
xp = []
xn = []
xf = [] 

# data
def main():
    print()

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

    print()
if __name__ == '__main__':
        main()

#plot
fig, ax = plt.subplots()
plt.scatter(xp, n, 1, c='Blue')
plt.scatter(xn, n)
plt.scatter(xf, n)
plt.savefig('FibTimes')
