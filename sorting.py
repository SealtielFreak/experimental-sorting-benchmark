def colomossort(elements):
    """Colomos sort."""
    _min, _max = [], []
    length = len(elements)

    if length <= 1:
        return elements
    elif length == 2:
        if elements[0] > elements[1]:
            return [elements[1], elements[0]]

        return elements

    m = sum(elements) / length

    for v in elements:
        if v > m:
            _max.append(v)
        else:
            _min.append(v)

    return colomossort(_min) + colomossort(_max)


def gravitysort(elements):
    """Gravity sort."""
    max_value = max(elements)
    rows = len(elements)
    grid = [[0] * max_value for _ in range(rows)]

    for col, num in enumerate(elements):
        for row in range(rows):
            if num > 0:
                grid[row][col] = 1
                num -= 1

    sorted_arr = []
    for col in range(max_value):
        count = 0
        for row in range(rows):
            if grid[row][col] == 1:
                count += 1
        sorted_arr.extend([col + 1] * count)

    return sorted_arr


def radixsort(elements):
    """Radix sort."""

    def countingsort(arr, exp1):
        n = len(arr)

        output = [0] * (n)

        count = [0] * (10)

        for i in range(0, n):
            index = arr[i] // exp1
            count[index % 10] += 1

        for i in range(1, 10):
            count[i] += count[i - 1]

        i = n - 1
        while i >= 0:
            index = arr[i] // exp1
            output[count[index % 10] - 1] = arr[i]
            count[index % 10] -= 1
            i -= 1

        i = 0
        for i in range(0, len(arr)):
            arr[i] = output[i]

    max1 = max(elements)

    exp = 1
    while max1 / exp >= 1:
        countingsort(elements, exp)
        exp *= 10

    return elements


def mergesort(elements):
    """Merge sort."""
    if len(elements) > 1:
        mid = len(elements) // 2

        left = elements[:mid]

        right = elements[mid:]

        mergesort(left)

        mergesort(right)

        i = j = k = 0

        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
                elements[k] = left[i]
                i += 1
            else:
                elements[k] = right[j]
                j += 1
            k += 1

        while i < len(left):
            elements[k] = left[i]
            i += 1
            k += 1

        while j < len(right):
            elements[k] = right[j]
            j += 1
            k += 1

    return elements


def quicksort(elements):
    """Quick sort."""
    if len(elements) <= 1:
        return elements
    else:
        pivot = elements[0]
        left = [x for x in elements[1:] if x < pivot]
        right = [x for x in elements[1:] if x >= pivot]

        return quicksort(left) + [pivot] + quicksort(right)


def countsort(elements):
    """Count sort."""
    max_element = max(elements)
    count = [0] * (max_element + 1)

    for element in elements:
        count[element] += 1

    for i in range(1, len(count)):
        count[i] += count[i - 1]

    output = [0] * len(elements)

    for i in range(len(elements) - 1, -1, -1):
        output[count[elements[i]] - 1] = elements[i]
        count[elements[i]] -= 1

    return output


def bucketsort(elements):
    """Bucket sort."""
    num_buckets = len(elements)

    buckets = [[] for _ in range(num_buckets)]

    for num in elements:
        bucket_index = int(num * num_buckets)
        buckets[bucket_index].append(num)

    # Python sort algorithm default
    for bucket in buckets:
        bucket.sort()

    sorted_arr = []
    for bucket in buckets:
        sorted_arr.extend(bucket)

    return sorted_arr


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
