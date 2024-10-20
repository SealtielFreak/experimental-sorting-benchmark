def insertion_sort(arr, low, high):
    for i in range(low + 1, high + 1):
        key = arr[i]
        j = i - 1

        while j >= low and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1

        arr[j + 1] = key

    return arr


def median_of_three(arr, low, high):
    mid = (low + high) // 2

    if arr[low] > arr[mid]:
        arr[low], arr[mid] = arr[mid], arr[low]
    if arr[low] > arr[high]:
        arr[low], arr[high] = arr[high], arr[low]
    if arr[mid] > arr[high]:
        arr[mid], arr[high] = arr[high], arr[mid]

    return mid


def partition(arr, low, high):
    pivot_index = median_of_three(arr, low, high)
    pivot = arr[pivot_index]
    arr[pivot_index], arr[high] = arr[high], arr[pivot_index]
    i = low - 1

    for j in range(low, high):
        if arr[j] < pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]

    arr[i + 1], arr[high] = arr[high], arr[i + 1]

    return i + 1


def quicksort_sub(arr, low, high):
    if high - low < 10:
        insertion_sort(arr, low, high)
    elif low < high:
        pi = partition(arr, low, high)
        quicksort_sub(arr, low, pi - 1)
        quicksort_sub(arr, pi + 1, high)


def quicksort(arr):
    quicksort_sub(arr, 0, len(arr) - 1)

    return arr
