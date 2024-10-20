def radixsort(elements):
    """Radix sort."""

    def countingsort(arr, exp1):
        n = len(arr)

        output = [0] * (n)

        count = [0] * (10)

        for i in range(0, n):
            index = arr[i] // exp1
            count[index % 10] += 1

        for i in range(1, 10):
            count[i] += count[i - 1]

        i = n - 1
        while i >= 0:
            index = arr[i] // exp1
            output[count[index % 10] - 1] = arr[i]
            count[index % 10] -= 1
            i -= 1

        i = 0
        for i in range(0, len(arr)):
            arr[i] = output[i]

    max1 = max(elements)

    exp = 1
    while max1 / exp >= 1:
        countingsort(elements, exp)
        exp *= 10

    return elements
