def meadsort_c(elements):
    """Mead sort (Like C)"""

    def partition(arr, length, mead):
        if length <= 1:
            return arr

        if length == 2:
            if arr[0] > arr[1]:
                return [arr[1], arr[0]]

            return arr

        aux_array = [None] * length
        count_l, count_r = 0, 0
        acum_l, acum_r = 0, 0

        pivot_r, pivot_l = length - 1, 0

        for i in arr:
            if i > mead:
                aux_array[pivot_r] = i
                count_r += 1
                acum_r += i

                pivot_r -= 1
            else:
                aux_array[pivot_l] = i
                count_l += 1
                acum_l += i

                pivot_l += 1

        if count_l > 0:
            arr[:count_l] = partition(aux_array[:count_l], count_l, acum_l / count_l)

        if count_r > 0:
            arr[count_l:] = partition(aux_array[count_l:], count_r, acum_r / count_r)

        return arr

    length = len(elements)
    mead = sum(elements) / length

    return partition(elements, length, mead)


def meadsort(elements):
    """Mead sort (Like C with concat arrays)"""

    def partition(arr, length, mead):
        if length <= 1:
            return arr

        if length == 2:
            if arr[0] > arr[1]:
                return [arr[1], arr[0]]

            return arr

        aux_array = [None] * length
        count_l, count_r = 0, 0
        acum_l, acum_r = 0, 0

        pivot_r, pivot_l = length - 1, 0

        for i in arr:
            if i > mead:
                aux_array[pivot_r] = i
                count_r += 1
                acum_r += i

                pivot_r -= 1
            else:
                aux_array[pivot_l] = i
                count_l += 1
                acum_l += i

                pivot_l += 1

        left, right = [], []

        if count_l > 0:
            left = partition(aux_array[:count_l], count_l, acum_l / count_l)

        if count_r > 0:
            right = partition(aux_array[count_l:], count_r, acum_r / count_r)

        return left + right

    length = len(elements)
    mead = sum(elements) / length

    return partition(elements, length, mead)
