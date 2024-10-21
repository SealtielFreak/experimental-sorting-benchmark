def msort(elements, length, high, low, mead=None):
    """M. sort."""
    n = low

    elements[0] = low

    while True:
        n += 1

        elements[n] = n

        if n >= high:
            return elements
