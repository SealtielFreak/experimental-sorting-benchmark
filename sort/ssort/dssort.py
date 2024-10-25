import math


def dssortf(elements, length, high, low):
    """DS. sort (Floats)."""
    negative_series = low < 0

    if negative_series:
        length //= 2

    pivot_p, pivot_n = 0, 0
    n_positive_series = [[[], []] for _ in range(length)]
    n_negative_series = [[[], []] for _ in range(length)] if negative_series else []

    k_positive_series = []
    k_negative_series = []

    for e in elements:
        if abs(e) > length:
            if e < 0:
                k_negative_series.append(e)
            else:
                k_positive_series.append(e)
        else:
            isnegative = e < 0

            s_arr = n_negative_series if isnegative else n_positive_series

            en = math.floor(e)
            isinteger = en == e
            index = abs(en)
            s_arr = s_arr[index][1] if not isinteger else s_arr[index][0]

            s_arr.append(e)

            if index > pivot_p and isinteger:
                pivot_p = index + 1

            if index > pivot_n and isnegative:
                pivot_n = index + 1

    k_series = len(k_positive_series) > 0

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

    def _bubblesort(elements):
        """Bubble sort."""
        n = len(elements)

        swapped = False

        for i in range(n - 1):
            for j in range(0, n - i - 1):
                if elements[j] > elements[j + 1]:
                    swapped = True
                    elements[j], elements[j + 1] = elements[j + 1], elements[j]

            if not swapped:
                return elements

        return elements

    if low < 0:
        length //= 2

    n_arr_p = [[] for _ in range(length)]
    n_arr_n = [[] for _ in range(length)]

    k_arr = []
    nk_arr = []

    for e in elements:
        if abs(e) > length:
            if e < 0:
                nk_arr.append(e)
            else:
                k_arr.append(e)
        else:
            if e < 0:
                n_arr_n[abs(e)].append(e)
            else:
                n_arr_p[e].append(e)

    elements = _bubblesort(nk_arr) if len(nk_arr) > 0 else []

    for d in reversed(n_arr_n):
        elements += d

    for d in n_arr_p:
        elements += d

    elements += _bubblesort(k_arr) if len(k_arr) > 0 else []

    return elements
