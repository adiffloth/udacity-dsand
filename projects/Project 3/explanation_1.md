## Square Root of an Integer

We're looking for the largest number that when squared, results in a number that is not bigger than the input number.

We could naively start at 1, square it, compare to the input and increment until we exceed or equal the input number. This would be an O(n) algorithm, but we can do better with a binary search.

To implement the binary search, we define the search range from 1 to the number, since it's square root is certainly contained in that range. We calculate the midpoint between the upper and lower bound, then square it. 

If the square of the midpoint is the input number, then the midpoint is the exact square root. If the square is less than the number, but the next square (adding one to midpoint and squaring) causes us to overshoot the input number, then the current guess is correct since we're looking for the floor square root.

If the square of the midpoint is greater than the input number, then our current guess is too high and we recursively search in the lower half. Otherwise (the current guess is too low), we recursively search in the upper half.

Time complexity: The halving of the search array with each loop is what gives us O(log n) time complexity.

Space complexity: Since we're not creating any new variables other than single placeholders, the space complexity is O(1).