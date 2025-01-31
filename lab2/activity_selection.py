import matplotlib.pyplot as plt
import random

from lab2.utils import get_execution_time_iterative, get_execution_time_recursive


def activity_selection_recursive_greedy(start, finish, k, n):
    m = k + 1
    while m <= n and start[m] < finish[k]:
        m += 1
    if m <= n:
        return [m] + activity_selection_recursive_greedy(start, finish, m, n)
    else:
        return []


def activity_selection_iterative_greedy(start, finish):
    n = len(start)
    k = 0
    activities = [1]

    for m in range(1, n):
        if start[m] >= finish[k]:
            activities.append(m + 1)
            k = m

    return activities


def generate_activity_selection_problem(n, start_range=(0, 50), duration_range=(1, 20)):
    """
    Generates a random Activity Selection Problem with n activities.

    Parameters:
    - n (int): Number of activities.
    - start_range (tuple): Range for generating start times (min, max).
    - duration_range (tuple): Range for generating activity durations (min, max).

    Returns:
    - List of tuples (start, end) representing activities.
    """
    activities = []

    for _ in range(n):
        start = random.randint(*start_range)
        duration = random.randint(*duration_range)
        end = start + duration  # Ensuring end time is greater than start time
        activities.append((start, end))

    # Sorting by end time to align with the greedy algorithm's optimal approach
    activities.sort(key=lambda x: x[1])

    return activities


test_lengths = [10, 100, 400, 700, 1000]
starts = []
finishes = []

y_values_recursive = []
y_values_iterative = []

for n in test_lengths:
    activities = generate_activity_selection_problem(n)
    start = [x[0] for x in activities]
    finish = [x[1] for x in activities]

    starts.append(start)
    finishes.append(finish)

    y_values_iterative.append(get_execution_time_iterative(
        activity_selection_iterative_greedy, start, finish))
    y_values_recursive.append(get_execution_time_recursive(
        activity_selection_recursive_greedy, start, finish, 0))


# Plotting the results
plt.xlabel('Number of activities')
plt.ylabel('Execution time')
plt.title('Activity Selection Problem - Greedy Algorithm')
plt.plot(test_lengths, y_values_recursive, label='Recursive')
plt.plot(test_lengths, y_values_iterative, label='Iterative')
plt.grid(True)
plt.legend()
plt.show()
