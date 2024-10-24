def flip(elements, i):
    start = 0
    while start < i:
        elements[start], elements[i] = elements[i], elements[start]
        start += 1
        i -= 1


def find_max(elements, n):
    mi = 0
    for i in range(1, n):
        if elements[i] > elements[mi]:
            mi = i
    return mi


def pancakesort(elements):
    """Pancake sort."""
    curr_size = len(elements)
    while curr_size > 1:
        mi = find_max(elements, curr_size)
        if mi != curr_size - 1:
            flip(elements, mi)
            flip(elements, curr_size - 1)
        curr_size -= 1
    return elements
