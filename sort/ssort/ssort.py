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


