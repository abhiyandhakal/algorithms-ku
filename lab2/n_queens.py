import matplotlib.pyplot as plt
from lab2.utils import get_execution_time_min_span


def solve_nqueens_backtracking(n):
    def is_safe(board, row, col):
        for i in range(row):
            if board[i] == col or abs(board[i] - col) == abs(i - row):
                return False
        return True

    def solve(board, row):
        if row == n:
            return 1
        count = 0
        for col in range(n):
            if is_safe(board, row, col):
                board[row] = col
                count += solve(board, row + 1)
        return count

    return solve([-1] * n, 0)


def solve_nqueens_bruteforce(n):
    from itertools import permutations

    def is_valid(board):
        return all(abs(board[i] - board[j]) != j - i for i in range(len(board)) for j in range(i + 1, len(board)))

    return sum(1 for perm in permutations(range(n)) if is_valid(perm))


# test_sizes = [4, 5, 6, 7, 8, 9, 10]
test_sizes = [4, 5, 6, 7, 8, 9, 10]
y_values_backtracking, y_values_bruteforce = [], []

for n in test_sizes:
    y_values_backtracking.append(
        get_execution_time_min_span(solve_nqueens_backtracking, n))
    y_values_bruteforce.append(
        get_execution_time_min_span(solve_nqueens_bruteforce, n))

plt.xlabel('Board Size (N)')
plt.ylabel('Execution Time')
plt.title('N-Queens Problem: Backtracking vs. Brute Force')
plt.plot(test_sizes, y_values_backtracking, label='Backtracking')
plt.plot(test_sizes, y_values_bruteforce, label='Brute Force')
plt.grid(True)
plt.legend()
plt.show()
