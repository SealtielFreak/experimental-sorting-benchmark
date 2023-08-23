def issame(elements_a, elements_b):
    if len(elements_a) != len(elements_b):
        return False

    sorted_list1 = sorted(elements_a)
    sorted_list2 = sorted(elements_b)

    return sorted_list1 == sorted_list2


def issorted(elements):
    n = len(elements)

    for i in range(1, n):
        if elements[i - 1] > elements[i]:
            return False

    return True
