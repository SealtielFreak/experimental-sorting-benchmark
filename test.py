import random

from sort.ssort.ssort import ssort_nn, ssort_n


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
    DEFAULT_LENGTH = 50

    elements = [random.randint(n, DEFAULT_LENGTH) for n in range(-DEFAULT_LENGTH, DEFAULT_LENGTH)]
    elements = [*elements] + [*elements] + [*elements] + [*elements] + [*elements]
    random.shuffle(elements)

    elements_sorted = ssort_n([*elements], len(elements), max(elements), min(elements))

    assert samelist(elements_sorted, elements), "The list is no longer the same"
    assert issorted(elements_sorted), "Sorting failed"

    print("Success!")
