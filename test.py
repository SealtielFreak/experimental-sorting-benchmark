import random

from sort.ssort.dssort import usort


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


if __name__ == "__main__":
    DEFAULT_LENGTH = 2500

    elements = [n for n in range(-DEFAULT_LENGTH, DEFAULT_LENGTH)]
    elements = [*elements] + [*elements] + [*elements] + [30, 500, 40000] + [-50000]
    random.shuffle(elements)

    array_sorted = usort([*elements], len(elements), max(elements), min(elements))

    assert samelist(array_sorted, elements), "The list is no longer the same"
    assert issorted(array_sorted), "Sorting failed"

    print("Success!")
