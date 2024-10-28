def meadsort_series(elements, length, high, low):
    """Mead sort (Series)."""
    k_series = length * (length - 1)

    if length <= 1:
        return elements
    elif length == 2:
        if elements[0] > elements[1]:
            return [elements[1], elements[0]]

        return elements

    step = abs(low)
    series_length = step + length + high + 1
    series_excluded = [0] * series_length
    difference = 0

    left, right = [], []

    mead = sum(elements) / length

    for i, e in enumerate(elements):
        if e > mead:
            right.append(e)
        else:
            left.append(e)

        if series_excluded[e + step] == 0:
            series_excluded[e + step] += 1
            difference += 1

    if difference <= 1:
        return elements

    left = meadsort_series(left, len(left), max(left), min(left))
    right = meadsort_series(right, len(right), max(right), min(right))

    return left + right
