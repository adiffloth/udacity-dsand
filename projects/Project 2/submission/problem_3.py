import sys
import heapq
from collections import Counter

"""
Adapted from: https://www.kosbie.net/cmu/spring-16/15-112/notes/notes-data-compression.html
"""


class Node:
    def __init__(self, char=None, count=None):
        self.char = char
        self.count = count
        self.left = None
        self.right = None

    # Override the less-than comparator so that heapq sorts on a node's count
    def __lt__(self, other_node):
        return self.count < other_node.count

    # Override repr for printing Nodes as part of a list.
    def __repr__(self):
        return str(self.char) + ' ' + str(self.count)

    # Override str for printing standalone Nodes.
    __str__ = __repr__


def create_min_heap(data):

    # Use collections.Counter to count/groupby
    char_counts = Counter(data)

    # Create list of Nodes from Counter object
    huff_q = []
    for char, count in char_counts.items():
        huff_q.append(Node(char, count))

    # Turn it into a heap - Python is min heap.
    heapq.heapify(huff_q)

    return huff_q


def create_huffman_tree(huff_q):

    # Handle edge cases
    if len(huff_q) == 0:
        return None
    elif len(huff_q) == 1:
        new_node = Node()
        new_node.left = heapq.heappop(huff_q)
        return new_node

    # Pop out smallest two nodes, combine them together, reinsert into priority queue
    # Repeat until there is only the root node in the priority queue.
    # Return the root node, not the list.
    while len(huff_q) > 1:
        new_node = Node()
        new_node.left = left = heapq.heappop(huff_q)
        new_node.right = right = heapq.heappop(huff_q)
        new_node.count = left.count + right.count
        heapq.heappush(huff_q, new_node)

    return heapq.heappop(huff_q)


def assign_codes(huff_tree):

    # Dictionary to map chars to codes.
    huff_codes = dict()

    # Generate the codes for a given node in a Huffman tree.
    def gen_code(huff_node, code):

        # Base case
        if huff_node is None:
            return

        # We're at a leaf node, so add the char and the code that got us there to the dict.
        if huff_node.left is None and huff_node.right is None:
            huff_codes[huff_node.char] = code

        # Recurse on the left branch, adding a 0 to the code.
        gen_code(huff_node.left, code + '0')

        # Recurse on the right branch, adding a 1 to the code.
        gen_code(huff_node.right, code + '1')

    # Generate the encoding dict for this Huffman tree and return it.
    gen_code(huff_tree, '')
    return huff_codes


def huffman_encoding(data):

    if data is None:
        return None, Node()

    # Create min_heap
    huff_q = create_min_heap(data)

    # Make a Huffman tree
    huff_tree = create_huffman_tree(huff_q)

    # Create codes for Huffman tree
    # Implement as depth-first traversal
    huff_dict = assign_codes(huff_tree)

    # Encode the input string and return it.len
    encoded_str = ''
    for char in data:
        encoded_str += huff_dict[char]
    return encoded_str, huff_tree


def huffman_decoding(data, tree):

    if data is None:
        return None
    decoded_str = ''

    # Read each 0/1 in the input.
    # Traverse left/right down the tree until you hit a leaf node.
    # That's the next char in the decoded string.
    current_node = tree  # Start at the root of the tree.
    for code in data:  # Loop through the encoded string.
        if code == '0':  # Code is 0 so follow the left branch.
            current_node = current_node.left
        elif code == '1':  # Code is 1 so follow the right branch.
            current_node = current_node.right
        if current_node.left is None and current_node.right is None:  # This is a leaf Node
            decoded_str += current_node.char  # Add the char of the leaf node to the decoded string
            current_node = tree  # Restart at the root node of the tree

    return decoded_str


if __name__ == "__main__":

    # Test 1 - positive test
    codes = {}

    a_great_sentence = "The bird is the word"

    print("The size of the data is: {}\n".format(sys.getsizeof(a_great_sentence)))
    print("The content of the data is: {}\n".format(a_great_sentence))

    encoded_data, tree = huffman_encoding(a_great_sentence)

    print("The size of the encoded data is: {}\n".format(sys.getsizeof(int(encoded_data, base=2))))
    print("The content of the encoded data is: {}\n".format(encoded_data))

    decoded_data = huffman_decoding(encoded_data, tree)

    print("The size of the decoded data is: {}\n".format(sys.getsizeof(decoded_data)))
    print("The content of the encoded data is: {}\n".format(decoded_data))

    # Test 2 - positive test from the problem statement.
    input_str = 'AAAAAAABBBCCCCCCCDDEEEEEE'
    encoded_str = '1010101010101000100100111111111111111000000010101010101'
    assert huffman_encoding(input_str)[0] == encoded_str
    assert huffman_decoding(*huffman_encoding(input_str)) == input_str

    # Test 3 - empty input string
    input_str = ''
    assert huffman_decoding(*huffman_encoding(input_str)) == input_str

    # Test 4 - None input
    input_str = None
    assert huffman_decoding(*huffman_encoding(input_str)) == input_str

    # Test 5 - long input
    input_str = """We hold these truths to be self-evident, that all men are created equal, that they are endowed by their Creator with certain unalienable Rights, that among these are Life, Liberty and the pursuit of Happiness. — That to secure these rights, Governments are instituted among Men, deriving their just powers from the consent of the governed, — That whenever any Form of Government becomes destructive of these ends, it is the Right of the People to alter or to abolish it, and to institute new Government, laying its foundation on such principles and organizing its powers in such form, as to them shall seem most likely to effect their Safety and Happiness."""
    assert huffman_decoding(*huffman_encoding(input_str)) == input_str
    print("The size of the data is: {}".format(sys.getsizeof(input_str)))
    print("The size of the encoded data is: {}\n".format(sys.getsizeof(int(huffman_encoding(input_str)[0], base=2))))

    # Test 6 - single character input
    input_str = 'a'
    assert huffman_decoding(*huffman_encoding(input_str)) == input_str
    input_str = 'aaaaaaaaaaa'
    assert huffman_decoding(*huffman_encoding(input_str)) == input_str

    print('Tests passed')
