def usort(elements, length, high, low):
    """U. sort."""
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

    n_arrp = [[] for _ in range(length)]
    n_arrn = [[] for _ in range(length)]

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
                n_arrn[abs(e)].append(e)
            else:
                n_arrp[e].append(e)

    elements = _bubblesort(nk_arr) if len(nk_arr) > 0 else []

    for d in reversed(n_arrn):
        elements += d

    for d in n_arrp:
        elements += d

    elements += _bubblesort(k_arr)

    return elements
