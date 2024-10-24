import math
import random


def ssortf(array, length, high, low):
    step_low = math.ceil(low)
    step = abs(math.ceil(low))
    length = math.ceil(step + high + length)
    subarray = [[0, []] for _ in range(length)]
    keys = []

    for n in array:
        index = math.ceil(n) + step

        if isinstance(n, float):
            subarray[index][1].append(n)

            if len(subarray[index][1]) == 1:
                keys.append(index)

        else:
            subarray[index][0] += 1

        if subarray[index][0] == 1:
            keys.append(index)

    auxarray = []

    for n, k in enumerate(keys):
        i, floats = subarray[k]

        while i != 0:
            auxarray.append(n + step_low)

            if i <= 1:
                break

            i -= 1

        if len(floats) != 0:
            floats.sort()

            auxarray += floats

    return auxarray


def ssort(array, length, high, low):
    step = abs(low)
    subarray = [0] * (step + high + length)

    for n in array:
        subarray[n + step] += 1

    auxarray = []

    for n, i in enumerate(subarray):
        while i != 0:
            auxarray.append(n - step)

            if i <= 1:
                break

            i -= 1

    return auxarray


if __name__ == "__main__":
    DEFAULT_LENGTH = 100

    array = [random.randint(0, 1000) for n in range(DEFAULT_LENGTH)]
    random.shuffle(array)
    print("Array unsorted:", array)

    array_sorted = ssortf(array, len(array), max(array), min(array))
    print("Array sorted:", array_sorted)

    array.sort()
    print("Array sorted:", array)
