from operator import mul
from functools import reduce


def product(items):
    results = list()
    for index, item in enumerate(items):
        temp = items.copy()
        del temp[index]

        results.append(reduce(mul, temp))

    print(results)
    return results


test_cases = [
    [1, 2, 3, 4, 5],
    [3, 2, 1]
]

for test_case in test_cases:
    product(test_case)
