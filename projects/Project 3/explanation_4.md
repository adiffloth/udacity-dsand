## Dutch National Flag

I solved this using the counting sort algorithm. This algorithm works when there are a small number of possible values to be sorted, in this case 3.

The single pass through the input list is used to count up the occurrences of each of the three possible values. This is O(n) and is performed once.

After the counts are obtained, the sorted result is created by making a string of 0s, 1s and 2s of the corresponding lengths based on our counts. This is O(1) since there is a constant number of possible values.

Overall the time complexity is one pass O(n). The space complexity is O(n) - the size of the returned list.