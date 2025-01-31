import matplotlib.pyplot as plt
import random
import time

# Las Vegas Quicksort Implementation


def quicksort(arr):
    if len(arr) <= 1:
        return arr
    else:
        pivot = random.choice(arr)
        less_than_pivot = [x for x in arr if x < pivot]
        equal_to_pivot = [x for x in arr if x == pivot]
        greater_than_pivot = [x for x in arr if x > pivot]
        return quicksort(less_than_pivot) + equal_to_pivot + quicksort(greater_than_pivot)

# Deterministic Quicksort Implementation


def deterministic_quicksort(arr):
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[len(arr) // 2]
        less_than_pivot = [x for x in arr if x < pivot]
        equal_to_pivot = [x for x in arr if x == pivot]
        greater_than_pivot = [x for x in arr if x > pivot]
        return deterministic_quicksort(less_than_pivot) + equal_to_pivot + deterministic_quicksort(greater_than_pivot)

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
las_vegas_times = []
deterministic_times = []

# Run tests for each array size
for size in test_sizes:
    test_array = generate_random_array(size)

    # Measure Las Vegas Quicksort time
    lv_time = measure_execution_time(quicksort, test_array)
    las_vegas_times.append(lv_time)

    # Measure Deterministic Quicksort time
    det_time = measure_execution_time(deterministic_quicksort, test_array)
    deterministic_times.append(det_time)

# Plot results
plt.figure(figsize=(10, 6))
plt.plot(test_sizes, las_vegas_times, label="Las Vegas Quicksort", marker="o")
plt.plot(test_sizes, deterministic_times,
         label="Deterministic Quicksort", marker="o")
plt.xlabel("Input Size (Number of Elements)")
plt.ylabel("Execution Time (seconds)")
plt.title("Las Vegas vs Deterministic Quicksort Performance")
plt.legend()
plt.grid(True)
plt.show()
