def meadsort(elements):
    def partition(arr, length, mead):
        if length <= 1:
            return arr

        if length == 2:
            if arr[0] > arr[1]:
                return [arr[1], arr[0]]

            return arr

        left, right = [], []
        pivot_l, pivot_r = 0, 0
        acum_l, acum_r = 0, 0

        for i in arr:
            if i > mead:
                right.append(i)
                pivot_r += 1
                acum_r += i
            else:
                left.append(i)
                pivot_l += 1
                acum_l += i

        left = partition(left, pivot_l, acum_l / pivot_l)
        right = partition(right, pivot_r, acum_r / pivot_r)

        return left + right

    length = len(elements)
    mead = sum(elements) / length

    return partition(elements, length, mead)
