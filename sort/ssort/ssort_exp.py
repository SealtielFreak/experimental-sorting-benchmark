import math
import random


def getdecimals(f: float) -> int:
    decimal = len(str(f).split(".")[1])
    return int("1" + ("0" * decimal))


def casttointegers(array, decimals):
    return [*map(lambda x: math.ceil(x * decimals), array)]


def casttofloats(array, decimals):
    return [*map(lambda x: x / decimals, array)]


def ssortf(array, length, high, low):
    step = abs(math.ceil(low))
    length = math.ceil(step + high + length)
    subarray = [[0, []] for _ in range(length)]

    for n in array:
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

    array = [-n / 10 for n in range(DEFAULT_LENGTH)]
    random.shuffle(array)

    print(array)
    array_sorted = ssortf(array, len(array), max(array), min(array))

    print(array_sorted)

    array.sort()
    print(array)

    print(len(array))
    print(len(array_sorted))
