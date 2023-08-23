#!/usr/bin/env python3
import pyperf

DEFAULT_LENGTH = 25


create_setup = lambda length: f"""
import random
import sorting

LENGTH = {length}

elements = list(range(LENGTH))
random.shuffle(elements)
"""

create_stmt = lambda name: f"""
sorted_elements = sorting.{name}(elements)
"""

teardown = """
import validtest

assert validtest.issame(sorted_elements, elements), "The list is no longer the same"
assert validtest.issorted(sorted_elements), "Sorting failed"
"""


runner = pyperf.Runner()


runner.timeit("Radix sort",
              setup=create_setup(DEFAULT_LENGTH),
              stmt=create_stmt("radixsort"),
              teardown=teardown)


runner.timeit("Merge sort",
              setup=create_setup(DEFAULT_LENGTH),
              stmt=create_stmt("mergesort"),
              teardown=teardown)
