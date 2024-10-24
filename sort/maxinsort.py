def maxinsort(elements):
    """Maxin sort."""
    end = len(elements)

    while True:
        m = elements.index(max(elements[:end]))
        elements[end - 1], elements[m] = elements[m], elements[end - 1]

        end -= 1

        if end <= 1:
            break

    return elements
