import math


def dssortf(elements, length, high, low):
    """DS. sort (Floats)."""
    if low < 0:
        length //= 2

    pivot_p, pivot_n = 0, 0
    n_arr_p = [[[], []] for _ in range(length)]
    n_arr_n = [[[], []] for _ in range(length)]

    k_arr = []
    nk_arr = []
    
    max_p, max_n = 0, 0

    for e in elements:
        if abs(e) > length:
            if e < 0:
                nk_arr.append(e)
            else:
                k_arr.append(e)
        else:
            isnegative = e < 0

            s_arr = n_arr_n if isnegative else n_arr_p

            en = math.floor(e)
            isinteger = en == e
            index = abs(en)
            s_arr = s_arr[index][1] if not isinteger else s_arr[index][0]

            s_arr.append(e)
            
            if index > pivot_p and isinteger:
                pivot_p = index + 1
                
            if index > pivot_n and isnegative:
                pivot_n = index + 1
    
    elements = []
    
    nk_arr.sort()
    elements += nk_arr
    
    n_arr_n = n_arr_n[:pivot_n + 1]
    for elms in reversed(n_arr_n):
        integers, floats = elms
        
        elements += integers
        
        floats.sort()
        elements += floats
        
    n_arr_p = n_arr_p[:pivot_p]
    for elms in n_arr_p:
        integers, floats = elms
        
        elements += integers
        
        floats.sort()
        elements += floats
    
    k_arr.sort()
    elements += k_arr

    return elements


def dssort(elements, length, high, low):
    """DS. sort."""
    def _bubblesort(elements):
        """Bubble sort."""
        n = len(elements)

        swapped = False

        for i in range(n - 1):
            for j in range(0, n - i - 1):
                if elements[j] > elements[j + 1]:
                    swapped = True
                    elements[j], elements[j + 1] = elements[j + 1], elements[j]

            if not swapped:
                return elements

        return elements

    if low < 0:
        length //= 2

    n_arr_p = [[] for _ in range(length)]
    n_arr_n = [[] for _ in range(length)]

    k_arr = []
    nk_arr = []

    for e in elements:
        if abs(e) > length:
            if e < 0:
                nk_arr.append(e)
            else:
                k_arr.append(e)
        else:
            if e < 0:
                n_arr_n[abs(e)].append(e)
            else:
                n_arr_p[e].append(e)

    elements = _bubblesort(nk_arr) if len(nk_arr) > 0 else []

    for d in reversed(n_arr_n):
        elements += d

    for d in n_arr_p:
        elements += d

    elements += _bubblesort(k_arr) if len(k_arr) > 0 else []

    return elements
