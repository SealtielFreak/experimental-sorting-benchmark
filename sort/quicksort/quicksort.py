def partition(arr, low, high):
    pivot = arr[high]

    i = low - 1

    for j in range(low, high):
        if arr[j] <= pivot:
            i = i + 1

            (arr[i], arr[j]) = (arr[j], arr[i])

    (arr[i + 1], arr[high]) = (arr[high], arr[i + 1])

    return i + 1


def quicksort(elements, low=None, high=None):
    """Quick sort."""

    if low is None:
        low = 0

    if high is None:
        high = len(elements) - 1

    if low < high:
        pi = partition(elements, low, high)

        quicksort(elements, low, pi - 1)
        quicksort(elements, pi + 1, high)

    return elements
