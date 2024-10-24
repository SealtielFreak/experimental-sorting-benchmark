def heapsort(elements):
    """Heap sort."""

    def heapify(arr, n, i):
        largest = i
        left = 2 * i + 1
        right = 2 * i + 2

        if left < n and arr[left] > arr[largest]:
            largest = left

        if right < n and arr[right] > arr[largest]:
            largest = right

        if largest != i:
            arr[i], arr[largest] = arr[largest], arr[i]
            heapify(arr, n, largest)

    n = len(elements)

    for i in range(n // 2 - 1, -1, -1):
        heapify(elements, n, i)

    for i in range(n - 1, 0, -1):
        elements[i], elements[0] = elements[0], elements[i]
        heapify(elements, i, 0)

    return elements
