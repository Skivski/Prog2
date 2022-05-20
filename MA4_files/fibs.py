from integer import Integer
from numba import njit
from time import perf_counter as pc
import multiprocessing as mp

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

n = [20, 25, 27]

def main():

    for i in n:
        print()
        start = pc()
        o = fib_pure_py(i)
        end = pc()
        print(f'*** Fibbonaci {i} = {o} ***')
        print(f'Time for pure python  {end-start}')
        

        start = pc()
        p = fib_numba_py(i)
        end = pc()
        print(f'Time for numba python: {end-start}')
        
        
        f = Integer(i)
        start = pc()
        f.fib()
        end = pc()
        print(f'Time for C++: {end-start}')
    print()

if __name__ == '__main__':
        main() 
