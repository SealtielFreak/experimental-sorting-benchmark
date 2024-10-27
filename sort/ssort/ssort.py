import math


def ssortf(elements, length, high, low):
    """S. sort (Floats)."""
    step = abs(math.ceil(low))
    length = math.ceil(step + high + length)
    subarray = [[0, []] for _ in range(length)]

    for n in elements:
        index = math.ceil(n) + step

        if isinstance(n, float):
            subarray[index][1].append(n)
        else:
            subarray[index][0] += 1

    auxarray = []

    for n, (i, floats) in enumerate(subarray):
        while i != 0:
            auxarray.append(n - step)

            if i <= 1:
                break

            i -= 1

        if len(floats) != 0:
            floats.sort()

            auxarray += floats

    return auxarray


def ssort(elements, length, high, low):
    """S. sort (Classic)."""
    step = abs(low)
    subarray_length = high + length if high > length else length + step if step > length else length
    subarray = [0] * subarray_length

    for n in elements:
        subarray[n + step] += 1

    pivot = 0

    for n, i in enumerate(subarray):
        for _ in range(i):
            elements[pivot] = n - step
            pivot += 1

    return elements


def ssort_n(elements, length, high, low):
    """S. sort (N)."""
    step = abs(low)
    subarray_length = high + length if high > length else length + step if step > length else length
    subarray = [[] for _ in range(subarray_length)]

    for n in elements:
        subarray[n + step].append(n)

    elements = []

    for d in subarray:
        elements += d

    """
    An alternative to unite the reconstructed chains is:
        return list(chain(*subarray))
    """

    return elements


def ssort_nn(elements, length, high, low):
    """S. sort (NN)."""
    step = abs(low)

    if length <= 1:
        return elements

    series_length = length


    # k_series = length * (length - 1)
    p_series = [0] * series_length
    n_series = [0] * series_length
    k_series = []

    for n in elements:
        if n > length:
            k_series.append(n)
        else:
            if n < 0:
                n_series[n + step] += 1
            else:
                p_series[n + step] += 1

    elements = []

    n_cumulative = 0
    n_autosum = sum(n_series)

    for i, d in enumerate(n_series):
        elements += [i - step] * d
        n_cumulative += d

        if n_cumulative >= n_autosum:
            break

    p_cumulative = 0
    p_autosum = sum(p_series)

    for i, d in enumerate(p_series):
        elements += [i] * d
        p_cumulative += d

        if p_cumulative >= p_autosum:
            break

    return elements
