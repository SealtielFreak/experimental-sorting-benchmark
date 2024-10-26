def insertionsort(elements):
    """Insertion sort."""
    for i in range(1, len(elements)):
        key = elements[i]
        j = i - 1

        while j >= 0 and key < elements[j]:
            elements[j + 1] = elements[j]
            j -= 1

        elements[j + 1] = key

    return elements
