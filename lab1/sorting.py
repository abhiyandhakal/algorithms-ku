import numpy as np
import matplotlib.pyplot as plt
from lab1.utils import get_execution_time


def bubble_sort(arr):
    for _ in range(len(arr)):
        for j in range(len(arr)-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]


def selection_sort(arr):
    for i in range(len(arr)):
        min_index = i
        for j in range(i+1, len(arr)):
            if arr[j] < arr[min_index]:
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]


def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i-1
        while j >= 0 and key < arr[j]:
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = key


def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr)//2
        L = arr[:mid]
        R = arr[mid:]

        merge_sort(L)
        merge_sort(R)

        i = j = k = 0

        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1

        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1

        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1


def quick_sort(arr, low, high):
    if low < high:
        pi = partition(arr, low, high)

        quick_sort(arr, low, pi-1)
        quick_sort(arr, pi+1, high)


def partition(arr, low, high):
    i = low - 1
    pivot = arr[high]

    for j in range(low, high):
        if arr[j] < pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]

    arr[i+1], arr[high] = arr[high], arr[i+1]
    return i+1


def heapify(arr, n, i):
    largest = i
    l = 2 * i + 1
    r = 2 * i + 2

    if l < n and arr[i] < arr[l]:
        largest = l

    if r < n and arr[largest] < arr[r]:
        largest = r

    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, n, largest)


def heap_sort(arr):
    n = len(arr)

    for i in range(n//2, -1, -1):
        heapify(arr, n, i)

    for i in range(n-1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        heapify(arr, i, 0)


x_values = np.array([10, 100, 400, 700, 1000])

arrays = [np.random.randint(0, 1000, x) for x in x_values]

print("Arrays generated successfully")

y_values_bubble_sort = []
y_values_selection_sort = []
y_values_insertion_sort = []
y_values_merge_sort = []
y_values_quick_sort = []
y_values_heap_sort = []

for i in range(len(x_values)):
    y_values_bubble_sort.append(
        get_execution_time(bubble_sort, arrays[i].copy()))

    y_values_selection_sort.append(
        get_execution_time(selection_sort, arrays[i].copy()))

    y_values_insertion_sort.append(
        get_execution_time(insertion_sort, arrays[i].copy()))

    y_values_merge_sort.append(
        get_execution_time(merge_sort, arrays[i].copy()))

    y_values_quick_sort.append(
        get_execution_time(quick_sort, arrays[i].copy()))

    y_values_heap_sort.append(get_execution_time(heap_sort, arrays[i].copy()))


plt.xlabel('Array size')
plt.ylabel('Execution time')

plt.title('Sorting algorithms comparison')

plt.plot(x_values, y_values_bubble_sort, label='Bubble Sort')
plt.plot(x_values, y_values_selection_sort, label='Selection Sort')
plt.plot(x_values, y_values_insertion_sort, label='Insertion Sort')
plt.plot(x_values, y_values_merge_sort, label='Merge Sort')
plt.plot(x_values, y_values_quick_sort, label='Quick Sort')
plt.plot(x_values, y_values_heap_sort, label='Heap Sort')
plt.grid(True)
plt.legend()
plt.show()
