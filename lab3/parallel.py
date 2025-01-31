import matplotlib.pyplot as plt
import random
import time
from multiprocessing import Pool, cpu_count

# Normal Quicksort Implementation


def quicksort(arr):
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[len(arr) // 2]
        less_than_pivot = [x for x in arr if x < pivot]
        equal_to_pivot = [x for x in arr if x == pivot]
        greater_than_pivot = [x for x in arr if x > pivot]
        return quicksort(less_than_pivot) + equal_to_pivot + quicksort(greater_than_pivot)

# Parallel Quicksort Implementation


def parallel_quicksort(arr):
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[len(arr) // 2]
        less_than_pivot = [x for x in arr if x < pivot]
        equal_to_pivot = [x for x in arr if x == pivot]
        greater_than_pivot = [x for x in arr if x > pivot]

        with Pool(cpu_count()) as pool:
            sorted_parts = pool.map(
                quicksort, [less_than_pivot, greater_than_pivot])

        return sorted_parts[0] + equal_to_pivot + sorted_parts[1]

# Generate random test arrays of varying sizes


def generate_random_array(size):
    return [random.randint(1, 1000000) for _ in range(size)]

# Measure execution time for a given sorting algorithm


def measure_execution_time(sort_function, arr):
    start_time = time.time()
    sort_function(arr)
    return time.time() - start_time


# Sizes of the arrays to test
test_sizes = [10**2, 10**3, 10**4, 10**5]
normal_times = []
parallel_times = []

# Run tests for each array size
for size in test_sizes:
    test_array = generate_random_array(size)

    # Measure Normal Quicksort time
    norm_time = measure_execution_time(quicksort, test_array)
    normal_times.append(norm_time)

    # Measure Parallel Quicksort time
    par_time = measure_execution_time(parallel_quicksort, test_array)
    parallel_times.append(par_time)

# Plot results
plt.figure(figsize=(10, 6))
plt.plot(test_sizes, normal_times, label="Normal Quicksort", marker="o")
plt.plot(test_sizes, parallel_times, label="Parallel Quicksort", marker="o")
plt.xlabel("Input Size (Number of Elements)")
plt.ylabel("Execution Time (seconds)")
plt.title("Normal vs Parallel Quicksort Performance")
plt.legend()
plt.grid(True)
plt.show()
