## Huffman encoding

Huffman encoding is a compression algorithm that uses a tree to assign codes to characters. The key insight is that by assigning shorter codes to characters that appear more frequently in the text, the resulting encoding will take up less space than if every character takes up 8 bits. Using a tree allows us to have variable size codes for each char without necessitating the use of a space-wasting delimiter.

I started with a Node object that has attributes the character represented by this Node, the count of the frequency with which this character appears in the text, and pointers to the left and right children Nodes in the Huffman Tree. I overrode the < comparator so that we could have a way of comparing Nodes on the count attribute. I also overrode string and repr so we could get visual representations of the Nodes.

The first step is to use Counter() from collections to get the count of every character in the text. Then I create a list of Nodes from the dict of character counts and turn it into a priority queue with Python's heapq. This gives me a min heap, which is very useful here because it will easily let me pop() the Node with the lowest frequency.

Once we have our min heap, we pop the two smallest (least frequent) Nodes, add up their frequencies, and use it to create a new Node with that frequency and the two popped children as left and right Nodes, then push the new Node back onto the min heap. We repeat this until the min heap consists of just the root node.

The next step consists of assigning binary codes to each char in the Huffman tree. To do this, we recursively follow the branches of the tree, appending a 0 to the code when we follow a left branch and a 1 when we follow a right branch. When we reach a leaf node, we add the leaf node's char and the bread crumb of 1s and 0s to the encoding dict. Once we've traversed the entire tree, our encoding tree is done.

In the final encoding step, we iterate through the plain text, use the coding dict to look up each char's code, and add the code to the encoded text.

To decode, we iterate through each 0/1 in the encoded string, following the prescribed path down the Huffman tree until we hit a leaf node. When we hit a leaf node, we record the node's char as the next char in the decoded string, reset our tree to the root node, get the next 0/1 from the encoded string and repeat until the entire encoded string is decoded.

### Time Complexity:
- collections.Counter() - O(n), where n is the number of chars in the input string. Performed once.
- create initial list - O(m), where m in the number of distinct chars in the input string. This operates on the list of distinct chars, not the original input.
- heapq.heapify() - O(m), performed once. 
- create_huffman_tree: heapq.heappop() - O(log m), performed (m-1) times, results in O(m log m)
- assign_codes() - O(m). This will traverse the entire tree, but the size of the tree is bounded by the number of possible chars. Does not grow with n.
- encoding step: does a dict lookup, which is O(1), for each char in the string, resulting in O(n).

Two ways to look at this. 

First, what is time complexity wrt the number of distinct chars. This is O(n log n), driven by the (n-1) iterations of popping and combining nodes to create the huffman tree. (n here is the number of distinct chars)

Second is time complexity wrt to the overall task. ie: what is the time complexity as the input text grows, not as the distinct-character space grows. This is O(n), driven by the Counter() step and the actual encoding of the text. (n here is the total number of chars in the input text)

So overall, I think the answer is that time complexity is O(n) where n is the length of the input string. The input string can grow arbitrarily large and will dominate over the set of distinct characters, which will be much smaller in any practical scenario.

### Space Complexity
The min heap and the Huffman tree are all bounded by the number of distinct chars in the alphabet being used and do not grow with the size of the input string, so the additional space required is O(1).
