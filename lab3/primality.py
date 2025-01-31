import matplotlib.pyplot as plt
import random
from lab3.utils import get_execution_time


def is_prime_simple(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True


def is_prime_fermat(n, k=5):
    if n < 2:
        return False
    for _ in range(k):
        a = random.randint(2, n - 1)
        if pow(a, n - 1, n) != 1:
            return False
    return True


def is_prime_miller_rabin(n, k=5):
    if n < 2:
        return False
    if n in (2, 3):
        return True
    if n % 2 == 0:
        return False
    r, d = 0, n - 1
    while d % 2 == 0:
        r += 1
        d //= 2
    for _ in range(k):
        a = random.randint(2, n - 2)
        x = pow(a, d, n)
        if x in (1, n - 1):
            continue
        for _ in range(r - 1):
            x = pow(x, 2, n)
            if x == n - 1:
                break
        else:
            return False
    return True


test_numbers = [random.randint(10**(i-1), 10**i) for i in range(2, 7)]
y_values_simple, y_values_fermat, y_values_miller_rabin = [], [], []

for n in test_numbers:
    y_values_simple.append(get_execution_time(is_prime_simple, n))
    y_values_fermat.append(get_execution_time(is_prime_fermat, n))
    y_values_miller_rabin.append(get_execution_time(is_prime_miller_rabin, n))

plt.xlabel('Random Numbers (N)')
plt.ylabel('Execution Time')
plt.title('Primality Testing: Simple vs. Fermat vs. Miller-Rabin')
plt.plot(test_numbers, y_values_simple, label='Simple')
plt.plot(test_numbers, y_values_fermat, label='Fermat')
plt.plot(test_numbers, y_values_miller_rabin, label='Miller-Rabin')
plt.grid(True)
plt.legend()
plt.show()
