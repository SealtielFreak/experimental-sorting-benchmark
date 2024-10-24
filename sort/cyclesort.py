def cyclesort(elements):
    """Cyclic sort."""
    for start in range(0, len(elements) - 1):
        item = elements[start]
        pos = start

        for i in range(start + 1, len(elements)):
            if elements[i] < item:
                pos += 1

        if pos == start:
            continue

        while item == elements[pos]:
            pos += 1
        elements[pos], item = item, elements[pos]

        while pos != start:
            pos = start
            for i in range(start + 1, len(elements)):
                if elements[i] < item:
                    pos += 1

            while item == elements[pos]:
                pos += 1
            elements[pos], item = item, elements[pos]

    return elements
