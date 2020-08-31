## Search in a Rotated Array

The naive approach would be to perform an O(n) scan through the array, but we would be ignoring the partial sorting that exists in the data.

Another approach would be to iterate through the array until the inversion is found, then split the array into two at the inversion. The two resulting arrays would be strictly increasing, and we could use binary search on both of those independently. The binary searches are O(log n) and could be done in parallel, but the iteration to find the inversion is O(n), so overall this is O(n).

Another, better approach could be to use binary search to find the inversion, then use the same approach as above. This would be O(log n) overall, but requires two sequential O(log n) passes. I was looking for a way to do a single O(log n) pass through the data, so I did not follow this approach.

The implementation I chose relies on the key insight that if you split a rotated sorted array anywhere, one of the halves will be monotonically increasing (actually strictly increasing in this case). It's possible that both halves could be strictly increasing, if you happen to split at the inversion, but that doesn't matter.

If you take a half that is strictly increasing, you can easily determine by looking at the first and last elements whether your target, if it is present, could possibly be in this half. If the target is in the range of the strictly increasing half, then recurse on that half. If the target is not in the range of the strictly increasing side, then it is possible that it is in the other side, so recurse on the other half. Repeat this until the target is found or the list is exhausted.

The time complexity of this approach is O(log n) since we are splitting the array in half on each recursive call. The space complexity is also O(log n) since there will be log(n) recursive calls in the call stack.