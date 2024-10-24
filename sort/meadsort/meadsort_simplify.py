def meadsort(elements):
    """Mead (Colomos) sort (simplify)."""

    length = len(elements)

    if length <= 1:
        return elements
    elif length == 2:
        if elements[0] > elements[1]:
            return [elements[1], elements[0]]

        return elements

    mead = sum(elements) / length

    left = [x for x in elements if x < mead]
    right = [x for x in elements if x >= mead]

    return meadsort(left) + meadsort(right)
