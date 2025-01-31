import time


def get_execution_time(sort_func, input, n=10):
    sum = 0

    for _ in range(n):
        t0 = time.time()
        if sort_func.__name__ == 'quick_sort':
            sort_func(input, 0, len(input) - 1)
        else:
            sort_func(input)
        t1 = time.time()
        sum += t1 - t0

    return sum / n
