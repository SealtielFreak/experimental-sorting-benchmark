import math


def ssortf(elements, length, high, low):
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
    step = abs(low)
    subarray = [0] * (step + high + length)

    for n in elements:
        subarray[n + step] += 1

    auxarray = []

    for n, i in enumerate(subarray):
        while i != 0:
            auxarray.append(n - step)

            if i <= 1:
                break

            i -= 1

    return auxarray
