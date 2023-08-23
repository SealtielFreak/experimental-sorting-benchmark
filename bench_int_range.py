#!/usr/bin/env python3
import inspect
import random

import pyperf

import sorting
import testing

runner = pyperf.Runner()

for n in (2 ** n for n in range(12, 24, 4)):
    elements = list(range(n))
    random.shuffle(elements)

    info_str = f"(length: {n}, max: {max(elements)}, min: {min(elements)})"

    for name, func in inspect.getmembers(sorting, inspect.isfunction):
        bench = runner.timeit(f"{name} {info_str}",
                              setup=testing.create_setup(elements),
                              stmt=testing.create_stmt(name),
                              teardown=testing.teardown)
