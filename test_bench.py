#!/usr/bin/env python3

import numpy as np
import math

import sorting
import validate


def sample_shuffle_range(length):
    elements = np.arange(length)
    np.random.shuffle(elements)

    return elements


def sample_negative_shuffle_range(length):
    elements = np.arange(-length, 0)
    np.random.shuffle(elements)

    return elements


def sample_reverse_range(length):
    elements = np.arange(length)

    return np.flip(elements)


def sample_uniform_small_range(length):
    elements = np.random.uniform(0, 1, size=length)
    np.random.shuffle(elements)

    return elements


def sample_shuffle_small_range(length):
    elements = list(range(length))

    sub = math.floor(length * 0.25)
    elm = elements[:sub]
    elements = elements[sub:]

    np.random.shuffle(elm)

    return np.array(elements + elm)


DEFAULT_LENGTH = 2 ** 12
DEFAULT_SAMPLE_GENERATOR = sample_shuffle_small_range


def test_meansortdeque(benchmark):
    elements = DEFAULT_SAMPLE_GENERATOR(DEFAULT_LENGTH)
    sorted_elements = benchmark(sorting.meansortdeque, elements)

    assert validate.issame(sorted_elements, elements), "The list is no longer the same"
    assert validate.issorted(sorted_elements), "Sorting failed"


def test_meansort(benchmark):
    elements = DEFAULT_SAMPLE_GENERATOR(DEFAULT_LENGTH)
    sorted_elements = benchmark(sorting.meansort, elements)

    assert validate.issame(sorted_elements, elements), "The list is no longer the same"
    assert validate.issorted(sorted_elements), "Sorting failed"


def test_meanbsort(benchmark):
    elements = DEFAULT_SAMPLE_GENERATOR(DEFAULT_LENGTH)
    sorted_elements = benchmark(sorting.meanbsort, elements)

    assert validate.issame(sorted_elements, elements), "The list is no longer the same"
    assert validate.issorted(sorted_elements), "Sorting failed"


def test_beadsort(benchmark):
    elements = DEFAULT_SAMPLE_GENERATOR(DEFAULT_LENGTH)
    sorted_elements = benchmark(sorting.beadsort, elements)

    assert validate.issame(sorted_elements, elements), "The list is no longer the same"
    assert validate.issorted(sorted_elements), "Sorting failed"


def test_bucketsort(benchmark):
    elements = DEFAULT_SAMPLE_GENERATOR(DEFAULT_LENGTH)
    sorted_elements = benchmark(sorting.bucketsort, elements)

    assert validate.issame(sorted_elements, elements), "The list is no longer the same"
    assert validate.issorted(sorted_elements), "Sorting failed"


def test_radixsort(benchmark):
    elements = DEFAULT_SAMPLE_GENERATOR(DEFAULT_LENGTH)
    sorted_elements = benchmark(sorting.radixsort, elements)

    assert validate.issame(sorted_elements, elements), "The list is no longer the same"
    assert validate.issorted(sorted_elements), "Sorting failed"


def test_mergesort(benchmark):
    elements = DEFAULT_SAMPLE_GENERATOR(DEFAULT_LENGTH)
    sorted_elements = benchmark(sorting.mergesort, elements)

    assert validate.issame(sorted_elements, elements), "The list is no longer the same"
    assert validate.issorted(sorted_elements), "Sorting failed"


def test_quicksort(benchmark):
    elements = DEFAULT_SAMPLE_GENERATOR(DEFAULT_LENGTH)
    sorted_elements = benchmark(sorting.quicksort, elements)

    assert validate.issame(sorted_elements, elements), "The list is no longer the same"
    assert validate.issorted(sorted_elements), "Sorting failed"


def test_countsort(benchmark):
    elements = DEFAULT_SAMPLE_GENERATOR(DEFAULT_LENGTH)
    sorted_elements = benchmark(sorting.countsort, elements)

    assert validate.issame(sorted_elements, elements), "The list is no longer the same"
    assert validate.issorted(sorted_elements), "Sorting failed"


def test_heapsort(benchmark):
    elements = DEFAULT_SAMPLE_GENERATOR(DEFAULT_LENGTH)
    sorted_elements = benchmark(sorting.heapsort, elements)

    assert validate.issame(sorted_elements, elements), "The list is no longer the same"
    assert validate.issorted(sorted_elements), "Sorting failed"


def test_bubblesort(benchmark):
    elements = DEFAULT_SAMPLE_GENERATOR(DEFAULT_LENGTH)
    sorted_elements = benchmark(sorting.bubblesort, elements)

    assert validate.issame(sorted_elements, elements), "The list is no longer the same"
    assert validate.issorted(sorted_elements), "Sorting failed"


def test_selectionsort(benchmark):
    elements = DEFAULT_SAMPLE_GENERATOR(DEFAULT_LENGTH)
    sorted_elements = benchmark(sorting.selectionsort, elements)

    assert validate.issame(sorted_elements, elements), "The list is no longer the same"
    assert validate.issorted(sorted_elements), "Sorting failed"


def test_shellsort(benchmark):
    elements = DEFAULT_SAMPLE_GENERATOR(DEFAULT_LENGTH)
    sorted_elements = benchmark(sorting.shellsort, elements)

    assert validate.issame(sorted_elements, elements), "The list is no longer the same"
    assert validate.issorted(sorted_elements), "Sorting failed"


def test_cocktailsort(benchmark):
    elements = DEFAULT_SAMPLE_GENERATOR(DEFAULT_LENGTH)
    sorted_elements = benchmark(sorting.cocktailsort, elements)

    assert validate.issame(sorted_elements, elements), "The list is no longer the same"
    assert validate.issorted(sorted_elements), "Sorting failed"


def test_cyclicsort(benchmark):
    elements = DEFAULT_SAMPLE_GENERATOR(DEFAULT_LENGTH)
    sorted_elements = benchmark(sorting.cyclicsort, elements)

    assert validate.issame(sorted_elements, elements), "The list is no longer the same"
    assert validate.issorted(sorted_elements), "Sorting failed"


def test_strandsort(benchmark):
    elements = DEFAULT_SAMPLE_GENERATOR(DEFAULT_LENGTH)
    sorted_elements = benchmark(sorting.strandsort, elements)

    assert validate.issame(sorted_elements, elements), "The list is no longer the same"
    assert validate.issorted(sorted_elements), "Sorting failed"


def test_combsort(benchmark):
    elements = DEFAULT_SAMPLE_GENERATOR(DEFAULT_LENGTH)
    sorted_elements = benchmark(sorting.combsort, elements)

    assert validate.issame(sorted_elements, elements), "The list is no longer the same"
    assert validate.issorted(sorted_elements), "Sorting failed"
