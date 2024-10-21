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
