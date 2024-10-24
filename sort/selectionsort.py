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
