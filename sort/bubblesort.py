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
