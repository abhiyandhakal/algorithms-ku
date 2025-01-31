import time


def get_execution_time_recursive(func, start, finish, k):
    sum = 0
    n = 10

    for _ in range(n):
        t0 = time.time()
        func(start, finish, k, len(start)-1)
        t1 = time.time()
        sum += t1 - t0

    return sum / n


def get_execution_time_iterative(func, start, finish):
    sum = 0
    n = 10

    for _ in range(n):
        t0 = time.time()
        func(start, finish)
        t1 = time.time()
        sum += t1 - t0

    return sum / n


def get_execution_time_min_span(func, n):
    sum = 0
    for _ in range(10):
        t0 = time.time()
        func(n)
        t1 = time.time()
        sum += t1 - t0

    return sum / 10
