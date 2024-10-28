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


def meadsort_fb(elements):
    """Mead sort (Fixed both)."""
    length = len(elements)
    left, right = [], []

    if length <= 1:
        return elements
    elif length == 2:
        if elements[0] > elements[1]:
            return [elements[1], elements[0]]

        return elements

    mead = sum(elements) / length
    difference_left, difference_right = elements[0], elements[0]
    last_left, last_right = elements[0], elements[0]
    difference_detected_left, difference_detected_right = False, False

    for v in elements:
        if v > mead:
            right.append(v)

            if not difference_detected_right and difference_right != last_right:
                difference_detected_right = True

            last_right = v
        else:
            left.append(v)

            if not difference_detected_left and difference_left != last_left:
                difference_detected_left = True

            last_left = v

    left = meadsort_fb(left) if difference_detected_left else left
    right = meadsort_fb(right) if difference_detected_right else right

    return left + right


def meadsort_p(elements):
    """Mead sort (Presorted)."""
    length = len(elements)
    left, right = [], []

    if length <= 1:
        return elements
    elif length == 2:
        if elements[0] > elements[1]:
            return [elements[1], elements[0]]

        return elements

    mead = sum(elements) / length
    pivot_left, pivot_right = elements[0], elements[0]
    last_left, last_right = elements[0], elements[0]
    sorted_l, sorted_r = True, True

    for v in elements:
        if v > mead:
            right.append(v)

            if sorted_r and not v >= last_right:
                sorted_r = False

            last_right = v
        else:
            left.append(v)

            if sorted_l and not v >= last_left:
                sorted_l = False

            last_left = v

    left = meadsort_p(left) if sorted_l else left
    right = meadsort_p(right) if sorted_r else right

    return left + right
