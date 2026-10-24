import matplotlib.pyplot as plt
import time
import random
import numpy as np
from numpy import random

def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr

def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr

def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr

if __name__ == "__main__":
    size1 = []
    Time1 = [] 
    size2 = []
    Time2 = [] 
    size3 = []
    Time3 = [] 
    for i in range(20):
        n1 = random.randint(1, 100000)
        n2 = random.randint(1, 100000)
        n3 = random.randint(1, 100000)
        size1 = np.append(size1, n1, axis = None)
        size2 = np.append(size2, n2, axis = None)
        size3 = np.append(size3, n3, axis = None)
        arr1 = np.random.randint(2000, size=(n1))
        arr2 = np.random.randint(2000, size=(n2))
        arr3 = np.random.randint(2000, size=(n3))
        start_time1 = time.time()
        bubble_sort(arr1)
        end_time1 = time.time()
        Time1 = np.append(Time1, (end_time1 - start_time1), axis = None)
        start_time2 = time.time()
        insertion_sort(arr2)
        end_time2 = time.time()
        Time2 = np.append(Time2, (end_time2 - start_time2), axis = None)
        start_time3 = time.time()
        selection_sort(arr1)
        end_time3 = time.time()
        Time1 = np.append(Time3, (end_time3 - start_time3), axis = None)
        # for i in arr:
        #     print(i, end=" ")

    plt.plot(size1, Time1)
    plt.show()
    plt.plot(size2, Time2)
    plt.show()
    plt.plot(size3, Time3)
    plt.show()
  