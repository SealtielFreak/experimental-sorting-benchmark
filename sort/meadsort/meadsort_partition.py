import random


def meadsort(elements):
    def partition(arr, length, mead):
        if length == 0:
            return [], []

        if length <= 2:
            if length == 1:
                return [], arr

            a, b = arr

            if a > b:
                return [b], [a]

            return [a], [b]

        min_left, max_right = [], []

        for i in arr:
            if i > mead:
                max_right.append(i)
            else:
                min_left.append(i)

        return min_left, max_right

    if len(elements) <= 1:
        return elements

    length = len(elements)
    mead = sum(elements) / length
    left, right = partition(elements, length, mead)

    left = meadsort(left)
    right = meadsort(right)

    return left + right


if __name__ == '__main__':
    ELEMENTS = list(range(50))
    random.shuffle(ELEMENTS)

    SORTED_ELEMENTS = meadsort([*ELEMENTS])

    print(ELEMENTS)
    print(SORTED_ELEMENTS)
