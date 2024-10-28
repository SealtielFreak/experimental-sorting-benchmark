def meadsort(elements):
    """Mead (Colomos) sort."""
    _min, _max = [], []
    length = len(elements)

    if length <= 1:
        return elements
    elif length == 2:
        if elements[0] > elements[1]:
            return [elements[1], elements[0]]

        return elements

    m_pivot = sum(elements) / length

    for v in elements:
        if v > m_pivot:
            _max.append(v)
        else:
            _min.append(v)

    _min = meadsort(_min)
    _max = meadsort(_max)

    return _min + _max


def meadsort_f(elements):
    """Mead sort (Fixed)."""
    length = len(elements)
    left, right = [], []

    if length <= 1:
        return elements
    elif length == 2:
        if elements[0] > elements[1]:
            return [elements[1], elements[0]]

        return elements

    mead = sum(elements) / length
    difference = elements[0]
    difference_detected = False

    for v in elements:
        if v > mead:
            right.append(v)
        else:
            left.append(v)

        if not difference_detected and difference != v:
            difference_detected = True

    if not difference_detected:
        return elements

    return meadsort_f(left) + meadsort_f(right)
