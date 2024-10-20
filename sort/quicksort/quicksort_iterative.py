def quicksort(elements, low=0, high=None):
    def partition(_arr, l, h):
        i = (l - 1)
        x = _arr[h]

        for j in range(l, h):
            if _arr[j] <= x:
                i = i + 1
                _arr[i], _arr[j] = _arr[j], _arr[i]

        _arr[i + 1], _arr[h] = _arr[h], _arr[i + 1]

        return i + 1

    if low is None:
        high = 0

    if high is None:
        high = len(elements) - 1

    size = high - low + 1
    stack = [0] * (size)

    top = -1

    top = top + 1
    stack[top] = low
    top = top + 1
    stack[top] = high

    while top >= 0:
        high = stack[top]
        top = top - 1
        low = stack[top]
        top = top - 1

        p = partition(elements, low, high)

        if p - 1 > low:
            top = top + 1
            stack[top] = low
            top = top + 1
            stack[top] = p - 1

        if p + 1 < high:
            top = top + 1
            stack[top] = p + 1
            top = top + 1
            stack[top] = high

    return elements
