def cocktailsort(elements):
    """Cocktail sort."""
    n = len(elements)
    swapped = True
    start = 0
    end = n - 1

    while (swapped == True):

        swapped = False

        for i in range(start, end):
            if elements[i] > elements[i + 1]:
                elements[i], elements[i + 1] = elements[i + 1], elements[i]
                swapped = True

        if swapped == False:
            break

        swapped = False

        end = end - 1

        for i in range(end - 1, start - 1, -1):
            if elements[i] > elements[i + 1]:
                elements[i], elements[i + 1] = elements[i + 1], elements[i]
                swapped = True

        start = start + 1

    return elements
