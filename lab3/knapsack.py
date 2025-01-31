import matplotlib.pyplot as plt
import random
import time

# Non-polynomial nature: solving the Knapsack problem exactly using brute force


def knapsack_bruteforce(weights, values, capacity, n):
    if n == 0 or capacity == 0:
        return 0
    if weights[n - 1] > capacity:
        return knapsack_bruteforce(weights, values, capacity, n - 1)
    else:
        return max(
            values[n - 1] +
            knapsack_bruteforce(
                weights, values, capacity - weights[n - 1], n - 1),
            knapsack_bruteforce(weights, values, capacity, n - 1)
        )

# Polynomial nature: decision version of the Knapsack problem (is there a subset with value >= target?)


def knapsack_decision(weights, values, capacity, target, n):
    if target <= 0:
        return True
    if n == 0 or capacity == 0:
        return False
    if weights[n - 1] > capacity:
        return knapsack_decision(weights, values, capacity, target, n - 1)
    else:
        return (
            knapsack_decision(weights, values, capacity - weights[n - 1], target - values[n - 1], n - 1) or
            knapsack_decision(weights, values, capacity, target, n - 1)
        )

# Generate random weights and values for the items


def generate_knapsack_data(n):
    weights = [random.randint(1, 100) for _ in range(n)]
    values = [random.randint(1, 500) for _ in range(n)]
    return weights, values

# Measure execution time for a given function


def measure_execution_time(func, *args):
    start_time = time.time()
    func(*args)
    return time.time() - start_time


# Sizes of the problem to test
test_sizes = [5, 10, 15, 20]
bruteforce_times = []
decision_times = []

# Run tests for each problem size
for size in test_sizes:
    weights, values = generate_knapsack_data(size)
    capacity = random.randint(50, 150)
    target = random.randint(50, 150)

    # Measure Brute Force Knapsack time
    bf_time = measure_execution_time(
        knapsack_bruteforce, weights, values, capacity, size)
    bruteforce_times.append(bf_time)

    # Measure Decision Knapsack time
    dec_time = measure_execution_time(
        knapsack_decision, weights, values, capacity, target, size)
    decision_times.append(dec_time)

# Plot results
plt.figure(figsize=(10, 6))
plt.plot(test_sizes, bruteforce_times, label="Brute Force (Exact)", marker="o")
plt.plot(test_sizes, decision_times, label="Decision Problem", marker="o")
plt.xlabel("Number of Items")
plt.ylabel("Execution Time (seconds)")
plt.title("Knapsack Problem: Exact vs Decision Problem")
plt.legend()
plt.grid(True)
plt.show()
