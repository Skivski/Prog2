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

n = range(31)
xp = []
xn = []
xf = [] 

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

    print('.png saved')
if __name__ == '__main__':
        main()

#plot
fig, ax = plt.subplots()
plt.scatter(n, xp, c='Green')
plt.scatter(n, xn, c='Blue')
plt.scatter(n, xf, c='Red')
plt.savefig('FibTimes')
