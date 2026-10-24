import matplotlib.pyplot as plt
import time
import random
import numpy as np
from numpy import random


def hybrid_merge_sort(arr, threshold):
    if len(arr) <= threshold:
        selection_sort(arr)
        return arr
    
    if len(arr) > 1:
        mid = len(arr) // 2
        left_half = arr[:mid]
        right_half = arr[mid:]

        hybrid_merge_sort(left_half, threshold)
        hybrid_merge_sort(right_half, threshold)

        i = j = k = 0
        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                arr[k] = left_half[i]
                i += 1
            else:
                arr[k] = right_half[j]
                j += 1
            k += 1

        while i < len(left_half):
            arr[k] = left_half[i]
            i += 1
            k += 1

        while j < len(right_half):
            arr[k] = right_half[j]
            j += 1
            k += 1
            
    return arr