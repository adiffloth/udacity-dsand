def mergesort(items):

    if len(items) <= 1:
        return items

    mid = len(items) // 2
    left = items[:mid]
    right = items[mid:]

    left = mergesort(left)
    right = mergesort(right)

    return merge(left, right)


def merge(left, right):

    merged = []
    left_index = 0
    right_index = 0

    while left_index < len(left) and right_index < len(right):
        if left[left_index] > right[right_index]:
            merged.append(right[right_index])
            right_index += 1
        else:
            merged.append(left[left_index])
            left_index += 1

    merged += left[left_index:]
    merged += right[right_index:]

    return merged


def rearrange_digits(input_list):
    """
    Rearrange Array Elements so as to form two number such that their sum is maximum.

    Args:
       input_list(list): Input List
    Returns:
       (int),(int): Two maximum sums
    """

    if len(input_list) <= 1:
        return input_list

    # Sort the list with merge sort
    sorted_list = mergesort(input_list)

    # Build the two numbers by pulling from the sorted list in reverse order and adding
    # alternatively to each number.
    first_str = ''
    second_str = ''
    for i, num in enumerate(reversed(sorted_list)):
        if i % 2 == 0:
            first_str += str(num)
        else:
            second_str += str(num)

    return int(first_str), int(second_str)


def test_function(test_case):
    output = rearrange_digits(test_case[0])
    solution = test_case[1]
    if sum(output) == sum(solution):
        print("Pass")
    else:
        print("Fail")


# Tests
print
test_function([[], []])  # Empty list
test_function([[1], [1]])  # One element list
test_function([[1, 2], [1, 2]])  # Two element list
test_function([[0, 0, 0, 0, 0], [0, 0]])  # Zeros
test_function([[1, 2, 3, 4, 5], [542, 31]])  # Multiple elements, in order
test_function([[4, 6, 2, 5, 9, 8], [964, 852]])  # Multiple elements, out of order
test_function([[5, 5, 7, 3, 9, 9, 9], [9953, 975]])  # Duplicate numbers
