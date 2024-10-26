import math


def dssortf(elements, length, high, low):
    """DS. sort (Floats)."""
    negative_series = low < 0
    k_series = high > length

    if negative_series:
        length //= 2

    pivot_p, pivot_n = 0, 0
    n_positive_series = [[[], []] for _ in range(length)]
    n_negative_series = [[[], []] for _ in range(length)] if negative_series else None

    k_positive_series = [] if k_series else None
    k_negative_series = [] if negative_series else None

    for e in elements:
        if abs(e) > length:
            if e < 0:
                k_negative_series.append(e)
            else:
                k_positive_series.append(e)
        else:
            is_negative = e < 0

            s_arr = n_negative_series if is_negative else n_positive_series

            en = math.floor(e)
            is_integer = en == e
            index = abs(en)
            s_arr = s_arr[index][1] if not is_integer else s_arr[index][0]

            s_arr.append(e)

            if index > pivot_p and is_integer:
                pivot_p = index + 1
            elif index > pivot_n and is_negative:
                pivot_n = index + 1

    elements = []
    n_positive_series = n_positive_series[:pivot_p + 1]

    if negative_series:
        n_negative_series = n_negative_series[:pivot_n + 1]

        k_negative_series.sort()
        elements += k_negative_series

        for elms in reversed(n_negative_series):
            integers, floats = elms

            elements += integers

            floats.sort()
            elements += floats

    for elms in n_positive_series:
        integers, floats = elms

        elements += integers

        floats.sort()
        elements += floats

    if k_series:
        k_positive_series.sort()
        elements += k_positive_series

    return elements


def dssort(elements, length, high, low):
    """DS. sort."""
    if low < 0:
        length //= 2

    pivot_p, pivot_n = 0, 0
    n_positive_series = [[] for _ in range(length)]
    n_negative_series = [[] for _ in range(length)]

    k_positive_series = []
    k_negative_series = []

    for e in elements:
        if abs(e) > length:
            if e < 0:
                k_negative_series.append(e)
            else:
                k_positive_series.append(e)
        else:
            is_negative = e < 0
            en = math.floor(e)
            is_integer = en == e
            index = abs(en)

            if e < 0:
                n_negative_series[index - 1].append(e)
            else:
                n_positive_series[index].append(e)

            if index > pivot_p and is_integer:
                pivot_p = index + 1
            elif index > pivot_n and is_negative:
                pivot_n = index + 1

    elements = []

    k_negative_series.sort()
    elements += k_negative_series

    n_negative_series = n_negative_series[:pivot_n + 1]

    for d in reversed(n_negative_series):
        elements += d

    n_positive_series = n_positive_series[:pivot_p + 1]

    for d in n_positive_series:
        elements += d

    k_positive_series.sort()
    elements += k_positive_series

    return elements
