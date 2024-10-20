def countsort(elements):
    """Count sort."""
    max_element = max(elements)
    count = [0] * (max_element + 1)

    for element in elements:
        count[element] += 1

    for i in range(1, len(count)):
        count[i] += count[i - 1]

    output = [0] * len(elements)

    for i in range(len(elements) - 1, -1, -1):
        output[count[elements[i]] - 1] = elements[i]
        count[elements[i]] -= 1

    return output
