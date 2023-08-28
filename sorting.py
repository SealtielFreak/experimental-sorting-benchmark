import collections


def meansortdeque(elements):
    """Mean sort (Colomos sort) with deque."""
    length = len(elements)
    _min, _max = collections.deque(), collections.deque()

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

    return meansort(_min) + meansort(_max)


def meansort(elements):
    """Mean sort (Colomos sort)."""
    length = len(elements)
    _min, _max = [], []

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

    return meansort(_min) + meansort(_max)


def meanbsort(elements, _limit=8):
    """Mean sort (Colomos sort) like bucket."""
    length = len(elements)
    _min, _max = [], []

    if length <= _limit:
        elements.sort()
        return elements

    m = sum(elements) / length

    for v in elements:
        if v > m:
            _max.append(v)
        else:
            _min.append(v)

    return meanbsort(_min, _limit) + meanbsort(_max, _limit)


def beadsort(elements):
    """Bead sort."""
    return_list = []

    transposed_list = [0] * max(elements)
    for num in elements:
        transposed_list[:num] = [n + 1 for n in transposed_list[:num]]

    for i in range(len(elements)):
        return_list.append(sum(n > i for n in transposed_list))

    return return_list[::-1]


def bucketsort(elements):
    """Bucket sort."""
    max_value = max(elements)
    size = max_value / len(elements)
    buckets = [[] for _ in range(len(elements))]

    for i in range(len(elements)):
        j = int(elements[i] / size)
        if j != len(elements):
            buckets[j].append(elements[i])
        else:
            buckets[len(elements) - 1].append(elements[i])

    for i in range(len(elements)):
        buckets[i] = sorted(buckets[i])

    result = []

    for i in range(len(elements)):
        result += buckets[i]

    return result


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


def bubblesort(elements):
    """Bubble sort."""
    n = len(elements)

    swapped = False

    for i in range(n - 1):
        for j in range(0, n - i - 1):
            if elements[j] > elements[j + 1]:
                swapped = True
                elements[j], elements[j + 1] = elements[j + 1], elements[j]

        if not swapped:
            return elements

    return elements


def selectionsort(elements):
    """Selection sort."""
    n = len(elements)

    for ind in range(n):
        min_index = ind

        for j in range(ind + 1, n):
            if elements[j] < elements[min_index]:
                min_index = j

        elements[ind], elements[min_index] = elements[min_index], elements[ind]

    return elements


def shellsort(elements):
    """Shell sort."""
    n = len(elements)
    gap = n // 2

    while gap > 0:
        j = gap
        while j < n:
            i = j - gap

            while i >= 0:
                if elements[i + gap] > elements[i]:
                    break
                else:
                    elements[i + gap], elements[i] = elements[i], elements[i + gap]

                i = i - gap
            j += 1

        gap = gap // 2

    return elements


def cocktailsort(elements):
    """Cocktail sort."""
    n = len(elements)
    swapped = True
    start = 0
    end = n - 1

    while (swapped == True):

        swapped = False

        for i in range(start, end):
            if elements[i] > elements[i + 1]:
                elements[i], elements[i + 1] = elements[i + 1], elements[i]
                swapped = True

        if swapped == False:
            break

        swapped = False

        end = end - 1

        for i in range(end - 1, start - 1, -1):
            if elements[i] > elements[i + 1]:
                elements[i], elements[i + 1] = elements[i + 1], elements[i]
                swapped = True

        start = start + 1

    return elements


def cyclicsort(elements):
    """Cyclic sort."""
    n = len(elements)
    i = 0

    while i < n:
        correct = elements[i] - 1
        if elements[i] != elements[correct]:
            elements[i], elements[correct] = elements[correct], elements[i]
        else:
            i += 1

    return elements


def strandsort(elements):
    """Strand sort."""

    def strand(inp):
        element, sub = 0, [inp.pop(0)]

        while element < len(inp):
            if inp[element] > sub[-1]:
                sub.append(inp.pop(element))
            else:
                element += 1

        return sub

    def merge(a, b):
        output = []

        while len(a) and len(b):
            if a[0] < b[0]:
                output.append(a.pop(0))
            else:
                output.append(b.pop(0))
                output += a
                output += b

        return output

    output = strand(elements)

    while len(elements):
        output = merge(output, strand(elements))

    return output


def combsort(elements):
    """Comb sort."""

    def get_next_gap(gap):
        gap = (gap * 10) // 13

        if gap < 1:
            return 1

        return gap

    n = len(elements)

    gap = n

    swapped = True

    while gap != 1 or swapped == 1:
        gap = get_next_gap(gap)

        swapped = False

        for i in range(0, n - gap):
            if elements[i] > elements[i + gap]:
                elements[i], elements[i + gap] = elements[i + gap], elements[i]
                swapped = True

    return elements
