def meadsort(elements, length=None, mead=None):
    if mead is None:
        mead = sum(elements) / length

    if length is None:
        lengt = len(elements)

    if length <= 1:
        return elements
    elif length == 2:
        if elements[0] > elements[1]:
            return [elements[1], elements[0]]

        return elements

    _min, _max = [], []
    pivot_l, pivot_r = 0, 0
    acum_l, acum_r = 0, 0

    for v in elements:
        if v > mead:
            _max.append(v)
            pivot_r += 1
            acum_r += v
        else:
            _min.append(v)
            pivot_l += 1
            acum_l += v

    _min = meadsort(_min, pivot_l, acum_l / pivot_l)
    _max = meadsort(_max, pivot_r, acum_r / pivot_r)

    return _min + _max
