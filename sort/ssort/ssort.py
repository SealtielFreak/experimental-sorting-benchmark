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
    def samelist(list1, list2):
        if len(list1) != len(list2):
            return False

        sorted_list1 = sorted(list1)
        sorted_list2 = sorted(list2)

        return sorted_list1 == sorted_list2


    def issorted(arr):
        n = len(arr)

        for i in range(1, n):
            if arr[i - 1] > arr[i]:
                return False

        return True


    DEFAULT_LENGTH = 5000

    elements = [n for n in range(DEFAULT_LENGTH)]
    random.shuffle(elements)

    array_sorted = ssortf(elements, len(elements), max(elements), min(elements))

    assert samelist(array_sorted, elements), "The list is no longer the same"
    assert issorted(array_sorted), "Sorting failed"

    print("Success!")
