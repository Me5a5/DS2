import numpy as np
import random
# Te quick sort is a divide and conquer aloritm. We coosse a pivot and partition around tis pivot
# The key process in quickSort is a partition(). There are three common algorithms to partition. All these algorithms have O(n) time complexity.

# Naive Partition: Here we create copy of the array. First put all smaller elements and then all greater. Finally we copy the temporary array back to original array. This requires O(n) extra space.
# Lomuto Partition:The logic is simple, we start from the leftmost element and keep track of the index of smaller (or equal) elements as i. While traversing, if we find a smaller element, we swap the current element with arr[i]. Otherwise, we ignore the current element. 
# Hoare's Partition: This is the fastest of all. Here we traverse array from both sides and keep swapping greater element on left with smaller on right while the array is not partitioned. Please refer Hoare's vs Lomuto for details.           

def partitionLom(arr, low, high, res):
    pivot = res
    arr[high], arr[pivot] = arr[pivot], arr[high]
    pivot  = high
    i = low - 1
    for j in range(low, high):
        if arr[j] < arr[pivot]:
            i += 1
            arr[i],arr[j] = arr[j], arr[i]
    arr[i+1], arr[high] = arr[high], arr[i+1]
    return i+1

def partitionHoa(arr, low, high, res):
    pivot = res
    arr[low], arr[pivot] = arr[pivot], arr[low]
    pivot  = low
    start = low - 1
    end = high + 1
    while True:
        start += 1
        while arr[start] < arr[pivot]:
            start += 1
        end -= 1
        while arr[end] > arr[pivot]:
            end -= 1
        if start >= end:
            return end 
        arr[start], arr[end] = arr[end], arr[start]

def Hoare(arr, low, high):
    if low < high: 
        res = random.randint(low, high + 1)
        
        # pi is the partition return index of pivot
        pi = partitionHoa(arr, low, high, res)
        
        # recursion calls for smaller elements
        # and greater or equals elements
        Hoare(arr, low, pi)
        Hoare(arr, pi + 1, high)

def Lomuto_sort(arr, low, high):
      if low < high:
        res = np.random.randint(low, high)
        
        # pi is the partition return index of pivot
        pi = partitionLom(arr, low, high, res)
        
        # recursion calls for smaller elements
        # and greater or equals elements
        Lomuto_sort(arr, low, pi - 1)
        Lomuto_sort(arr, pi + 1, high)

if __name__ == "__main__":
    arr1 = [10, 7, 8, 9, 1, 5]
    arr = [10, 7, 8, 9, 1, 5]
    n = len(arr)
    m = len(arr1)
    Lomuto_sort(arr, 0, n - 1)
    Hoare(arr1, 0, n-1)
    
    for val in arr:
        print(val, end=" ")
    for val in arr1:
            print(val, end=" ")


