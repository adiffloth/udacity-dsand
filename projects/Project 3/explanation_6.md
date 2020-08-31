## Unsorted Integer Array

Pretty straightforward. Initialize two variables to positive and negative infinity, iterate through the list, compare each item to the largest and smallest seen so far, replace as appropriate.

Time complexity is O(n) since we are doing a single full pass through the input data set.

Space complexity is O(1) since we are only creating two additional variables.