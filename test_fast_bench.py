import pyperf

from conf import create_stmt, run_all_bench, create_teardown, create_custom_stmt, create_load_stmt
from conf.files import load_file

DEFAULT_LENGTH_ARRAY = 10000

DEFAULT_SETUP = f"""
import random
import math

DEFAULT_LENGTH = {DEFAULT_LENGTH_ARRAY}

elements = [random.randint(n, DEFAULT_LENGTH) for n in range(-DEFAULT_LENGTH, DEFAULT_LENGTH)]
elements = [*elements] + [*elements] + [*elements] + [*elements] + [*elements]
random.shuffle(elements)
"""

ALL_STMT_TEST = {
    "S. sort (N)": create_custom_stmt("ssort_n", load_file("sort/ssort/ssort.py"), create_load_stmt("ssort_n")),
    # "K. Series sort": create_custom_stmt("kssort", load_file("sort/ssort/kssort.py"), create_load_stmt("kssort")),
    "Count sort": create_stmt("countsort", load_file("sort/countsort.py")),
    # "Flash sort": create_stmt("flashsort", load_file("sort/flashsort.py")),
    "Pigeonhole sort": create_stmt("pigeonholesort", load_file("sort/pigeonholesort.py")),
    # "Bubble sort": create_stmt("bubblesort", load_file("sort/bubblesort.py")),
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
