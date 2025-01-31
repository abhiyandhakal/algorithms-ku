import matplotlib.pyplot as plt
from lab3.utils import get_execution_time


def fibonacci_recursive(n):
    if n <= 1:
        return n
    return fibonacci_recursive(n - 1) + fibonacci_recursive(n - 2)


def fibonacci_dynamic(n, memo={}):
    if n in memo:
        return memo[n]
    if n <= 1:
        return n
    memo[n] = fibonacci_dynamic(n - 1, memo) + fibonacci_dynamic(n - 2, memo)
    return memo[n]


test_sizes = [5, 10, 15, 20, 25, 30, 35]
y_values_recursive, y_values_dynamic = [], []

for n in test_sizes:
    y_values_recursive.append(get_execution_time(fibonacci_recursive, n))
    y_values_dynamic.append(get_execution_time(fibonacci_dynamic, n))

plt.xlabel('N')
plt.ylabel('Execution Time')
plt.title('Fibonacci: Recursive vs. Dynamic Programming')
plt.plot(test_sizes, y_values_recursive, label='Recursive')
plt.plot(test_sizes, y_values_dynamic, label='Dynamic')
plt.grid(True)
plt.legend()
plt.show()
print(y_values_dynamic)
