create_setup = lambda elements: f"""
import sorting

elements = {elements}
"""

create_stmt = lambda name: f"""
sorted_elements = sorting.{name}(elements)
"""

teardown = """
import validate

assert validate.issame(sorted_elements, elements), "The list is no longer the same"
assert validate.issorted(sorted_elements), "Sorting failed"
"""
