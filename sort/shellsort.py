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
