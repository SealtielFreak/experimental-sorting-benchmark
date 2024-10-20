def flashsort(elements):
    """Flash sort."""

    n = len(elements)

    min_value, max_value = elements[0], elements[0]
    for i in range(1, n):
        if elements[i] > max_value: max_value = elements[i]
        if elements[i] < min_value: min_value = elements[i]
    if min_value == max_value: return

    import math
    m = max(math.floor(0.45 * n), 1)

    def get_bucket_id(value):
        return math.floor((m * (value - min_value)) / (max_value - min_value + 1))

    Lb = [0] * m
    for value in elements:
        Lb[get_bucket_id(value)] += 1

    for i in range(1, m):
        Lb[i] = Lb[i - 1] + Lb[i]

    def find_swap_index(b_id):
        for ind in range(Lb[b_id - 1], Lb[b_id]):
            if get_bucket_id(elements[ind]) != b_id: break
        return ind

    def arrange_bucket(i1, i2, b):
        for i in range(i1, i2):
            b_id = get_bucket_id(elements[i])
            while (b_id != b):
                s_ind = find_swap_index(b_id)
                elements[i], elements[s_ind] = elements[s_ind], elements[i]
                b_id = get_bucket_id(elements[i])
        return

    for b in range(0, m - 1):
        if b == 0:
            arrange_bucket(b, Lb[b], b)
        else:
            arrange_bucket(Lb[b - 1], Lb[b], b)

    def insertion_sort(array):
        for i in range(1, len(array)):
            temp = array[i]
            j = i - 1
            while j >= 0 and temp < array[j]:
                array[j + 1] = array[j]
                j -= 1
            array[j + 1] = temp
        return array

    for i in range(m):
        if i == 0:
            elements[i:Lb[i]] = insertion_sort(elements[i:Lb[i]])
        else:
            elements[Lb[i - 1]:Lb[i]] = insertion_sort(elements[Lb[i - 1]:Lb[i]])

    return elements
