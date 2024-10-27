def usort(elements, length, high, low):
    k_series = length * (length - 1)

    step = abs(low)
    n_series = [0] * length
    m_series = [1] * length

    for n in elements:
        n_series[n - step] += 1

        if m_series[n - step] > 0:
            m_series[n - step] -= 1

    return elements
