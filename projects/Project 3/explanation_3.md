## Rearrange Array Digits

To solve this problem, I first used merge sort to sort the input list, which is O(n log n). Then I iterated through the sorted list and appended the next number in the sorted list to the end of two strings, alternating between the two. This operation is O(n). By starting with the largest values, I made sure the most significant digits were the largest in the two resulting numbers, which guarantees the largest possible sum. By alternating between the two numbers, I ensure the lengths of the two numbers are not more than 1 in difference.

The time complexity is O(n log n), from the merge sort operation. The space complexity is O(n) since I'm creating a new sorted list rather than sorting in place.