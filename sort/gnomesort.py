def gnomesort(elements):
    """Gnome sort."""
    index = 0
    while index < len(elements):
        if index == 0 or elements[index] >= elements[index - 1]:
            index += 1
        else:
            elements[index], elements[index - 1] = elements[index - 1], elements[index]
            index -= 1
    return elements
