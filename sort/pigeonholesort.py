def pigeonholesort(elements):
    """Pigeonhole sort."""

    _min = min(elements)
    _max = max(elements)
    size = _max - _min + 1

    holes = [0] * size

    for x in elements:
        assert type(x) is int, "integers only please"
        holes[x - _min] += 1

    i = 0
    for count in range(size):
        while holes[count] > 0:
            holes[count] -= 1
            elements[i] = count + _min
            i += 1

    return elements
