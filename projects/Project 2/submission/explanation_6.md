## Union and intersection

I used the set functionality in Python to implement union and instersection for our linked list object. To accomplish this, I convert the linked lists to sets, which is O(n).

Then I use set.union() which is O(len(s1) + len(s2)), and set.intersection(), which is O(min(len(s1), len(s2))), where s1 and s2 are the two input sets.

Finally, I convert the output set to a linked list and return. By keeping track of the tail of the linked list, I avoid repeatedly traversing the linked list when performing the append.

The additional space used for union is O(len(s1) + len(s2)). For intersection, in the worst case, it is also O(len(s1) + len(s2)).