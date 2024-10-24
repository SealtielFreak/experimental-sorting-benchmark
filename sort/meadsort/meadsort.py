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

    m = sum(elements) / length

    for v in elements:
        if v > m:
            _max.append(v)
        else:
            _min.append(v)

    _min = meadsort(_min)
    _max = meadsort(_max)

    return _min + _max
