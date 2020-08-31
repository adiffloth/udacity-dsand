def rotated_array_search(input_list, number):
    """
    Find the index by searching in a rotated sorted array

    Args:
       input_list(array), number(int): Input array to search and the target
    Returns:
       int: Index or -1
    """

    if input_list in [None, []]:
        return -1

    return recursive_bin_search(input_list, number, 0, len(input_list) - 1)


def recursive_bin_search(input_list, target, left_idx, right_idx):

    # Found it on left, right or mid index.
    left_val = input_list[left_idx]
    if left_val == target:
        return left_idx

    right_val = input_list[right_idx]
    if right_val == target:
        return right_idx

    mid_idx = (left_idx + right_idx) // 2
    mid_val = input_list[mid_idx]
    if mid_val == target:
        return mid_idx

    # Exhausted the list and didn't find it.
    if left_idx == mid_idx:
        return -1

    if (left_val < mid_val):  # Left half is monotonic
        if left_val < target < mid_val:  # And it's in the range of the left half
            return recursive_bin_search(input_list, target, left_idx, mid_idx - 1)  # Recurse on left half
        else:  # It could be on the right side
            return recursive_bin_search(input_list, target, mid_idx + 1, right_idx)  # Recurse on the right half
    else:  # Right half is monotonic
        if mid_val < target < right_val:  # And it's in the range of the right half
            return recursive_bin_search(input_list, target, mid_idx + 1, right_idx)  # Recurse on right half
        else:  # It could be on the left half
            return recursive_bin_search(input_list, target, left_idx, mid_idx - 1)  # Recurse on left half


def linear_search(input_list, number):
    for index, element in enumerate(input_list):
        if element == number:
            return index
    return -1


def test_function(test_case):
    input_list = test_case[0]
    number = test_case[1]
    if linear_search(input_list, number) == rotated_array_search(input_list, number):
        return 'Pass'
    else:
        return 'Fail'


assert test_function([[6, 7, 8, 9, 10, 1, 2, 3, 4], 6]) == 'Pass'
assert test_function([[6, 7, 8, 9, 10, 1, 2, 3, 4], 1]) == 'Pass'
assert test_function([[6, 7, 8, 1, 2, 3, 4], 8]) == 'Pass'
assert test_function([[6, 7, 8, 1, 2, 3, 4], 1]) == 'Pass'
assert test_function([[6, 7, 8, 1, 2, 3, 4], 10]) == 'Pass'

# Empty list
assert test_function([[], 42]) == 'Pass'
# Single element list
assert test_function([[42], 42]) == 'Pass'
# Two element list, not rotated, found
assert test_function([[42, 50], 42]) == 'Pass'
# Two element list, not rotated, not found
assert test_function([[42, 50], 45]) == 'Pass'
# Two element list, rotated, found
assert test_function([[50, 42], 42]) == 'Pass'
# Two element list, rotated, not found
assert test_function([[50, 42], 45]) == 'Pass'

# Multiple element list, not rotated, found
assert test_function([[0, 10, 20, 30, 40, 50, 60, 70, 80, 90], 40]) == 'Pass'
# Multiple element list, not rotated, not found
assert test_function([[0, 10, 20, 30, 40, 50, 60, 70, 80, 90], 32]) == 'Pass'
# Multiple element list, rotated, found in left half
assert test_function([[30, 40, 50, 60, 70, 80, 90, 0, 10, 20], 40]) == 'Pass'
# Multiple element list, rotated, found in right half
assert test_function([[30, 40, 50, 60, 70, 80, 90, 0, 10, 20], 10]) == 'Pass'

print('Tests passed.')
