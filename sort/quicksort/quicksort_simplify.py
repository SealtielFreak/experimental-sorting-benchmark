def quicksort(elements):
    """Quick sort (Simplify)."""

    if len(elements) <= 1:
        return elements
    else:
        pivot = elements[0]
        left = [x for x in elements[1:] if x < pivot]
        right = [x for x in elements[1:] if x >= pivot]

        return quicksort(left) + [pivot] + quicksort(right)
