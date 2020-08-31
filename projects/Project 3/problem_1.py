def sqrt(number):
    """
    Calculate the floored square root of a number

    Args:
       number(int): Number to find the floored squared root
    Returns:
       int: Floored Square Root
    """

    # Handle edge cases.
    if number is None:
        return None
    if number < 0:
        return -1
    if number == 0:
        return 0

    return sqrt_bin_search(number, 1, number)


def sqrt_bin_search(target, lower, upper):
    # Recursive binary search for the square root of a target.
    midpt_guess = (lower + upper) // 2
    square = midpt_guess ** 2
    plus_one_square = (midpt_guess + 1) ** 2

    # The square of the current guess is exactly the target, or going one more
    # will be too much, so the current guess is right floor sqrt.
    if square <= target < plus_one_square:
        return midpt_guess

    # The target is less than the square of the current guess, so recursively
    # search the numbers to the left of the current midpoint guess.
    elif target < square:
        return sqrt_bin_search(target, lower, midpt_guess - 1)

    # The target is greater than, so recurse on the right side.
    else:
        return sqrt_bin_search(target, midpt_guess + 1, upper)


# Tests
assert 3 == sqrt(9)
assert 0 == sqrt(0)
assert 4 == sqrt(16)
assert 1 == sqrt(1)
assert 5 == sqrt(27)

assert sqrt(None) is None  # Test None
assert sqrt(-9) == -1  # Negative
assert sqrt(-8474) == -1  # Big negative
assert sqrt(0) == 0  # Base case
assert sqrt(1) == 1  # The other base case
assert sqrt(2) == 1  # Test floor
assert sqrt(3) == 1
assert sqrt(4) == 2  # Breakpoint
assert sqrt(5) == 2  # Test floor again
assert sqrt(6) == 2
assert sqrt(7) == 2
assert sqrt(8) == 2
assert sqrt(9) == 3  # Breakpoint
assert sqrt(81) == 9
assert sqrt(1764) == 42
assert sqrt(7142726233651801) == 84514651  # Large number

print('Tests passed.')
