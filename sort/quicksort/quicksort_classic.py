def quicksort(elements):
    """Quick sort (Classic)."""
    left, right = [], []
    length = len(elements)

    if length <= 1:
        return elements
    elif length == 2:
        if elements[0] > elements[1]:
            return [elements[1], elements[0]]

        return elements

    pivot = elements[0]

    for v in elements[1:]:
        if v > pivot:
            right.append(v)
        else:
            left.append(v)

    left = quicksort(left)
    right = quicksort(right)

    return left + [pivot] + right
