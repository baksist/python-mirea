import math
import random 
import time

def factorize(N):
    p = []
    for d in range(2, int(math.sqrt(N)) + 1):
        if N % d == 0:
            p.append(d)
            N = N // d
    if N > 1:
        p.append(N)
    return p

r_0 = 1000000000000
r_1 = r_0 * 10

n = 3
time_start = time.time()
while n > 0:
    r = random.randint(r_0, r_1)
    res = factorize(r)
    if len(res) == 1:
        time_end = time.time()
        print(f"{r}, {time_end - time_start:.3f} s")
        n -= 1
        time_start = time.time()

# for i in range(r_0, r_1):
#     factors = factorize(i)
#     if len(factors) == 1:
#         print(i)