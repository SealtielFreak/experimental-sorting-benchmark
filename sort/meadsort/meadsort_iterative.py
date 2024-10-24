import collections


def mead_sort(arr):
    def mead_partition(_arr):
        if len(_arr) == 0:
            return [], []

        if len(_arr) <= 2:
            if len(_arr) == 1:
                return [], _arr
            elif len(_arr) == 0:
                return [], []

            a, b = _arr

            if a > b:
                return [b], [a]

            return [a], [b]

        left, right = collections.deque(), collections.deque()
        mead = sum(_arr) / len(_arr)

        for n in _arr:
            if n > mead:
                right.append(n)
            else:
                left.append(n)

        return [*left], [*right]

    l_pivot, r_pivot = 0, len(arr)

    while True:
        _left, _right = mead_partition(arr[l_pivot:r_pivot])

        if not l_pivot >= r_pivot:
            arr[l_pivot:r_pivot] = _left + _right

        if l_pivot >= len(arr):
            break

        if r_pivot <= (l_pivot + 1):
            r_pivot = len(arr)
            l_pivot += 1
        else:
            l_pivot, r_pivot = l_pivot, len(_left)

    return arr
