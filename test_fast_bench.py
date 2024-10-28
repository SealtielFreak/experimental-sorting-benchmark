import pyperf

from conf import create_stmt, run_all_bench, create_teardown, create_custom_stmt, create_load_stmt
from conf.files import load_file

DEFAULT_LENGTH_ARRAY = 10000

DEFAULT_SETUP = f"""
import random
import math

DEFAULT_LENGTH = {DEFAULT_LENGTH_ARRAY}

elements = [random.randint(n, DEFAULT_LENGTH) for n in range(-DEFAULT_LENGTH, DEFAULT_LENGTH)]
elements = [*elements] + [*elements] + [*elements] + [*elements] + [*elements] + [*elements]
random.shuffle(elements)
"""

ALL_STMT_TEST = {
    "Quick sort": create_stmt("quicksort", load_file("sort/quicksort/quicksort_classic.py")),
    "Mead sort (F)": create_stmt("meadsort_f", load_file("sort/meadsort/meadsort.py")),
    "Mead sort (FF)": create_stmt("meadsort_ff", load_file("sort/meadsort/meadsort.py")),
    "Mead sort (K)": create_stmt("meadsort_k", load_file("sort/meadsort/meadsort.py")),
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
