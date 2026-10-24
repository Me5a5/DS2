import matplotlib.pyplot as plt
import time
import random
import numpy as np
from numpy import random

def max_heapify(arr, n, i):
    largest = i
    left = 2 * i + 1
    right = 2 * i + 2

    if left < n and arr[left] > arr[largest]:
        largest = left

    if right < n and arr[right] > arr[largest]:
        largest = right

    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        max_heapify(arr, n, largest)

def build_max_heap(arr):
    n = len(arr)
    for i in range(n // 2 - 1, -1, -1):
        max_heapify(arr, n, i)

def heap_sort(arr):
    n = len(arr)
    build_max_heap(arr)
    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        max_heapify(arr, i, 0)

if __name__ == "__main__":
    size = []
    Time = [] 
    for i in range(20):
        n = random.randint(1, 100000)
        size = np.append(size, n, axis = None)
        arr = np.random.randint(2000, size=(n))
        # arr = [38, 27, 43, 10]
        start_time = time.time()
        heap_sort(arr)
        end_time = time.time()
        Time = np.append(Time, (end_time - start_time), axis = None)
        # for i in arr:
        #     print(i, end=" ")

    plt.plot(size, Time)
    plt.show()
  