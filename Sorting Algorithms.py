""" Sort a list of elements using the Bubble Sort algorithm.
Args - arr: The list to be sorted.
Returns the sorted list.

The algorithm repeatedly iterates through the list, compares adjacent elements, and swaps them if they are in the wrong order.
    It terminates when no swaps are needed, meaning that the list is sorted.
"""

def bubble_sort(arr):
    sorted = False  #Flag for optimization, minimize unnecessary iterations

    while not sorted:
        sorted = True
        for i in range(0, len(arr)-1):
            if arr[i] > arr[i+1]:
                sorted = False
                arr[i], arr[i+1] = arr[i+1], arr[i]
    return arr



"""
  Sort a list of elements using Insertion Sort.
  Args - arr: The list of elements to be sorted.
  Returns the sorted list.

  The algorithm iteratively places each element of an unsorted list  into its correct position 
  within a sorted portion of the list. It considers each element as the key and compares it with the 
  elements in the sorted array, shifting them right until it finds 
  the correct position."""

def insertion_sort (arr):
    for i in range(len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr [j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j +1] = key

    return arr




"""Sort a list of elements using merge sort.
    Args - arr: The list of elements to be sorted.
    Returns the sorted list.
    
    The algorithm divides the list into smaller sublists, sorts each sublist individually,
    then merges them back to produce a sorted list."""

def merge_sort(arr):

    n = len(arr)
    if n <= 1:  # Terminate recursion when size is 1 or less
        return arr

    mid = len(arr) // 2
    left = merge_sort(arr[:mid])  # Recursive call to sort the left half
    right = merge_sort(arr[mid:])  # Recursive call to sort the right half

    return merge_sublists(left, right)


def merge_sublists(left, right):
    merged = []
    i = j = 0

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            merged.append(left[i])
            i += 1
        else:
            merged.append(right[j])
            j += 1

    merged += right[j:]  # Appends any remaining elements from the right sublist
    merged += left[i:]  # Appends any remaining elements from the left sublist

    return merged



"""Sorts a list of elements using Quick Sort.
    Args - arr: The list of elements to be sorted.
    Returns: the sorted list.

    Quick Sort recursively divides the list into two sublists based on a pivot element,
    sorting each individually. The pivot is chosen as the first element. 
    The sorted sublists are then concatenated."""

def quick_sort(arr):

    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[0]
        less = [x for x in arr[1:] if x <= pivot]
        more = [x for x in arr[1:] if x > pivot]
        return quick_sort(less) + [pivot] + quick_sort(more)



if __name__ == "__main__":
    arrays = [
        [7, 18, 12, 8, 9, 32],
        [5, 3, 7, 2, 5, 1, 7, 3],
        [-5, 8, -3, 0, 12, -7, 4],
        [],
        ["banana", "apple", "orange", "grape", "kiwi"],
        ["dog", "cat", "bird", "elephant", "fish"],
        ["python", "java", "javascript", "ruby", "c++", "swift"]
    ]

    sorting_functions = [
        bubble_sort,
        insertion_sort,
        merge_sort,
        quick_sort
    ]

    for sorting_function in sorting_functions:
        print(f"Testing {sorting_function.__name__}:")
        for arr in arrays:
            sorted_arr = sorting_function(arr.copy())

            if arr:
                print(f"Input array: {arr}")
                print(f"Sorted array: {sorted_arr}")
                print()