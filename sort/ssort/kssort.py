def kssort(elements, length, high, low):
    """K. Series sort."""
    step = abs(low)
    index_n_series = [0 for _ in range(length)]
    n_series = [None for _ in range(length)]

    for i, n in enumerate(elements):
        index_n_series[n - step] += 1
        index = (n + index_n_series[n - step]) - 1 - step

        n_series[index] = n

    return n_series


def kssort_s(elements, length, high, low):
    """K. Series sort. (S)"""
    step = abs(low)

    if high > length:
        raise "Out of range"

    if abs(low) > length:
        pass

    index_n_series = [0] * length
    index_p_series = [0] * length

    p_series = [[] for _ in range(length)]
    n_series = [[] for _ in range(length)]

    for i, n in enumerate(elements):
        index_p_series[n - step] += 1

        p_series[n - step].append(n)

    elements = []

    pivot_p, acum = 0, 0

    while pivot_p < len(p_series):
        if len(p_series[pivot_p]) == 0:
            jump = len(p_series[pivot_p - 1]) + p_series[pivot_p - 1][0]

            if p_series[jump] is None:
                pivot_p = acum
            else:
                pivot_p = jump


        elements += p_series[pivot_p]
        acum += index_p_series[pivot_p]

        pivot_p += 1

        if acum >= len(p_series):
            break

    return elements
