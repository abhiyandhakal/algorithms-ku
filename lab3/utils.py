import time


def get_execution_time(func, n):
    sum = 0
    for _ in range(10):
        t0 = time.time()
        func(n)
        t1 = time.time()
        sum += t1 - t0

    return sum / 10
