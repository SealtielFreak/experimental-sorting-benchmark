def oddevensort(elements):
    """Odd-Even sort."""
    sorted = False
    while not sorted:
        sorted = True
        for i in range(1, len(elements) - 1, 2):
            if elements[i] > elements[i + 1]:
                elements[i], elements[i + 1] = elements[i + 1], elements[i]
                sorted = False

        for i in range(0, len(elements) - 1, 2):
            if elements[i] > elements[i + 1]:
                elements[i], elements[i + 1] = elements[i + 1], elements[i]
                sorted = False

    return elements
