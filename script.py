"""
This module implements the merge sort algorithm and demonstrates its usage.
"""

def merge(arr, left, mid, right):
    """
    Merge two halves of an array in sorted order.
    """
    n1 = mid - left + 1
    n2 = right - mid

    left_half = [0] * n1
    right_half = [0] * n2

    for i in range(n1):
        left_half[i] = arr[left + i]
    for j in range(n2):
        right_half[j] = arr[mid + 1 + j]
    i = 0
    j = 0
    k = left
    while i < n1 and j < n2:
        if left_half[i] <= right_half[j]:
            arr[k] = left_half[i]
            i += 1
        else:
            arr[k] = right_half[j]
            j += 1
        k += 1

    while i < n1:
        arr[k] = left_half[i]
        i += 1
        k += 1

    while j < n2:
        arr[k] = right_half[j]
        j += 1
        k += 1

def merge_sort(arr, left, right):
    """
    Perform merge sort on the array.
    """
    if left < right:
        mid = (left + right) // 2

        merge_sort(arr, left, mid)
        merge_sort(arr, mid + 1, right)
        merge(arr, left, mid, right)

def print_list(arr):
    """
    Print elements of the array.
    """
    for i in arr:
        print(i, end=" ")
    print()
    if __name__ == "__main__":
    array = [12, 81, 33, 55, 6, 71]
    merge_sort(array, 0, len(array) - 1)
    print_list(array)
