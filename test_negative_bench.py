import pyperf

from conf import create_stmt, run_all_bench, create_teardown
from conf.files import load_file

DEFAULT_LENGTH_ARRAY = 100000

DEFAULT_SETUP = f"""
import random
import math

DEFAULT_LENGTH = {DEFAULT_LENGTH_ARRAY}

elements = [-n for n in range(DEFAULT_LENGTH)]
random.shuffle(elements)
"""

ALL_STMT_TEST = {
    "Mead sort": create_stmt("meadsort", load_file("sort/meadsort/meadsort.py")),
    "Mead sort (Like C)": create_stmt("meadsort", load_file("sort/meadsort/meadsort_like_c.py")),
    "Mead sort (Simplify)": create_stmt("meadsort", load_file("sort/meadsort/meadsort_simplify.py")),

    "Mead sort (Concat)": create_stmt("meadsort", load_file("sort/meadsort/meadsort_concat.py")),
    "Mead sort (Slide)": create_stmt("meadsort", load_file("sort/meadsort/meadsort_slide.py")),

    "Quick sort": create_stmt("quicksort", load_file("sort/quicksort/quicksort.py")),
    "Quick sort (Iterative)": create_stmt("quicksort", load_file("sort/quicksort/quicksort_iterative.py")),
    "Quick sort (Simplify)": create_stmt("quicksort", load_file("sort/quicksort/quicksort_simplify.py")),
    "Quick sort (Optimize)": create_stmt("quicksort", load_file("sort/quicksort/quicksort_optimze.py")),

    "Count sort": create_stmt("countsort", load_file("sort/countsort.py")),
    "Flash sort": create_stmt("flashsort", load_file("sort/flashsort.py")),
    "Pigeonhole sort": create_stmt("pigeonholesort", load_file("sort/pigeonholesort.py")),
    "Radix sort": create_stmt("radixsort", load_file("sort/radixsort.py")),
    "Tim sort": create_stmt("timsort", load_file("sort/timsort.py")),
}

if __name__ == "__main__":
    runner = pyperf.Runner()
    teardown = create_teardown()

    run_all_bench(
        runner,
        ALL_STMT_TEST,
        DEFAULT_SETUP,
        teardown
    )
