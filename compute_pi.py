from random import random
from time import perf_counter
 
def calPI(N = 100):
    hits = 0
    start = perf_counter()
    con=0
    for i in range(1, N*N+1):
        con=con+1
        print(con)
        x, y = random(), random()
        dist = pow(x ** 2 + y ** 2, 0.5)
        if dist <= 1.0:
            hits += 1
    pi = (hits * 4) / (N * N)
    use_time = perf_counter() - start
    return pi, use_time
 
PI, use_time = calPI(100000)
print('use Monte Carlo method to calculate PI: {}'.format(PI))
print('use time: {} s'.format(use_time))