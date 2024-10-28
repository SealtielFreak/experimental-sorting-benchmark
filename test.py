import random

from sort.meadsort.meadsort import meadsort_f


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
    elements = [0, 0, 1, 2, 0, 8, 0, 0, 1, 8, 3, -1, 10**100]
    random.shuffle(elements)

    elements_sorted = meadsort_f(elements)

    assert samelist(elements_sorted, elements), "The list is no longer the same"
    assert issorted(elements_sorted), "Sorting failed"

    print("Success!")
