def dumb(items, expected):
    """
    Dumb function for getting to the solution.
    Iterates through
    """
    print("Doing it dumb.")
    for fInd, first in enumerate(items):
        for sInd, second in enumerate(items):
            if fInd == sInd:
                continue
            current_sum = first + second
            if current_sum == expected:
                print(f"Dumb found! {first} at {fInd} ; {second} at {sInd}")
                return True

    return False


def smart(items, expected):
    """
    Smarter function for getting to the solution.
    Only iterates through the list once.

    Disclaimer: I watched the google vid about this.
    """

    print("Trying to be smart.")
    temp = set()
    for index, item in enumerate(items):
        if item in temp:
            print(f"Smart found! {item} at {index}, and complement in the set.")
            return True

        temp.add(expected - item)

    return False


# Assumptions:
# - No negative numbers
# - At least 2 items
# - Items not sorted
test_cases = [
    {"expected": 6, "items": [10, 7, 3, 7, 7, 3, 10]},
    {"expected": 10, "items": [10, 7, 3, 7, 7, 3, 10]},
]

for test_case in test_cases:
    print(f"Search for {test_case['expected']} as the sum of two items.")
    print(f"\tThe list: {test_case['items']}")
    print()
    dumb_result = dumb(test_case['items'], test_case['expected'])
    print(f"Result of dumb: {dumb_result}")
    smart_result = smart(test_case['items'], test_case['expected'])
    print(f"Result of smart: {smart_result}")
