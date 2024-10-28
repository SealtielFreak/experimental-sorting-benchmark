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


def meadsort_m(elements):
    """Mead sort (M)."""
    length = len(elements)

    if length <= 1:
        return elements
    elif length == 2:
        if elements[0] > elements[1]:
            return [elements[1], elements[0]]

        return elements

    _min, _mead, _max = [], [], []
    m_pivot = sum(elements) / length

    for v in elements:
        if v > m_pivot:
            _max.append(v)
        elif v < m_pivot:
            _min.append(v)
        else:
            _mead.append(v)

    return meadsort_m(_min) + _mead + meadsort_m(_max)


def meadsort_mf(elements):
    """Mead sort (MF)."""
    length = len(elements)

    if length <= 1:
        return elements
    elif length == 2:
        if elements[0] > elements[1]:
            return [elements[1], elements[0]]

        return elements

    _min, _mead, _max = [], [], []
    mead = sum(elements) / length
    pivot_l, pivot_r = elements[0], elements[0]
    det_left, det_right = False, False

    for v in elements:
        if v > mead:
            _max.append(v)

            if not det_right and v != pivot_r:
                det_right = True

            pivot_r = v
        elif v < mead:
            _min.append(v)

            if not det_left and v != pivot_l:
                det_left = True

            pivot_l = v
        else:
            _mead.append(v)

    _min = meadsort_mf(_min) if det_left else _min
    _max = meadsort_mf(_max) if det_right else _max

    return _min + _mead + _max


def meadsort_f(elements):
    """Mead sort (F)."""
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


def meadsort_ff(elements):
    """Mead sort (FF)."""
    length = len(elements)
    left, right = [], []

    if length <= 1:
        return elements
    elif length == 2:
        if elements[0] > elements[1]:
            return [elements[1], elements[0]]

        return elements

    mead = sum(elements) / length
    pivot_l, pivot_r = elements[0], elements[0]
    det_left, det_right = False, False

    for v in elements:
        if v > mead:
            right.append(v)

            if not det_right and v != pivot_r:
                det_right = True

            pivot_r = v
        else:
            left.append(v)

            if not det_left and v != pivot_l:
                det_left = True

            pivot_l = v

    left = meadsort_ff(left) if det_left else left
    right = meadsort_ff(right) if det_right else right

    return left + right


def meadsort_k(elements):
    """Mead sort (K)."""
    length = len(elements)
    left, right = [], []

    mead = sum(elements) / length
    pivot_l, pivot_r = elements[0], elements[0]
    det_left, det_right = False, False
    sort_left, sort_right = True, True

    for v in elements:
        if v > mead:
            right.append(v)

            if not det_right and v != pivot_r:
                det_right = True

            if sort_right and not v >= pivot_r:
                sort_right = False

            pivot_r = v
        else:
            left.append(v)

            if not det_left and v != pivot_l:
                det_left = True

            if sort_left and not v >= pivot_r:
                sort_left = False

            pivot_l = v

    left = meadsort_k(left) if det_left and not sort_left else left
    right = meadsort_k(right) if det_right and not sort_right else right

    return left + right


def meadsort_zk(elements):
    """Mead sort (ZK)."""
    length = len(elements)

    if length <= 1:
        return elements
    elif length == 2:
        if elements[0] > elements[1]:
            return [elements[1], elements[0]]

    _min, _mead, _max = [], [], []
    mead = sum(elements) / length
    pivot_l, pivot_r = elements[0], elements[0]
    det_left, det_right = False, False
    sort_left, sort_right = True, True

    for v in elements:
        if v > mead:
            _max.append(v)

            if not det_right and v != pivot_r:
                det_right = True

            if sort_right and not v >= pivot_r:
                sort_right = False

            pivot_r = v
        elif v < mead:
            _min.append(v)

            if not det_left and v != pivot_l:
                det_left = True

            if sort_left and not v >= pivot_r:
                sort_left = False

            pivot_l = v
        else:
            _mead.append(v)

    _min = meadsort_zk(_min) if det_left and not sort_left else _min
    _max = meadsort_zk(_max) if det_right and not sort_right else _max

    return _min + _mead + _max
