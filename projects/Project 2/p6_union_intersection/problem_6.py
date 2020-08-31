class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

    def __repr__(self):
        return str(self.value)


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def __str__(self):
        cur_head = self.head
        out_string = ""
        while cur_head:
            out_string += str(cur_head.value) + " -> "
            cur_head = cur_head.next
        return out_string

    def append(self, value):

        if self.head is None:
            self.head = Node(value)
            return

        node = self.head
        while node.next:
            node = node.next

        node.next = Node(value)

    def size(self):
        size = 0
        node = self.head
        while node:
            size += 1
            node = node.next

        return size


# Utility function to convert a linked list to a Python set.
# O(n)
def llist_to_set(llist):

    output_set = set()
    node = llist.head
    while node:
        output_set.add(node.value)
        node = node.next

    return output_set


# Utility function to convert a set to a linked list.
# Remember the location of the tail so you don't have to traverse the entire linked lis for every append.
# O(n)
def set_to_llist(input_set):

    llist = LinkedList()
    for value in input_set:
        if llist.head is None:
            llist.head = Node(value)
            llist.tail = llist.head  # when we only have 1 node, head and tail refer to the same node
        else:
            llist.tail.next = Node(value)  # attach the new node to the `next` of tail
            llist.tail = llist.tail.next  # update the tail

    return llist


def union(llist_1, llist_2):

    # Convert to sets
    set_1 = llist_to_set(llist_1)
    set_2 = llist_to_set(llist_2)

    # Perform set union
    union_set = set_1.union(set_2)

    # Convert to llist, return
    return set_to_llist(union_set)


def intersection(llist_1, llist_2):

    # Convert to sets
    set_1 = llist_to_set(llist_1)
    set_2 = llist_to_set(llist_2)

    # Perform set union
    intersect_set = set_1.intersection(set_2)

    # Convert to llist, return
    return set_to_llist(intersect_set)


# Test case 1 - Standard case with intersection
linked_list_1 = LinkedList()
linked_list_2 = LinkedList()

element_1 = [3, 2, 4, 35, 6, 65, 6, 4, 3, 23]
element_2 = [1, 7, 8, 9, 11, 21, 1, 2, 65]

for i in element_1:
    linked_list_1.append(i)

for i in element_2:
    linked_list_2.append(i)

print(union(linked_list_1, linked_list_2))
print(intersection(linked_list_1, linked_list_2))

# Test case 2 - No intersection
linked_list_3 = LinkedList()
linked_list_4 = LinkedList()

element_1 = [3, 2, 4, 35, 6, 65, 6, 4, 3, 23]
element_2 = [1, 7, 8, 9, 11, 21, 1]

for i in element_1:
    linked_list_3.append(i)

for i in element_2:
    linked_list_4.append(i)

print(union(linked_list_3, linked_list_4))
print(intersection(linked_list_3, linked_list_4))

# Test case 3 - One empty linked list
linked_list_3 = LinkedList()
linked_list_4 = LinkedList()

element_1 = [3, 2, 4, 35, 6, 65, 6, 4, 3, 23]
element_2 = []

for i in element_1:
    linked_list_3.append(i)

for i in element_2:
    linked_list_4.append(i)

print(union(linked_list_3, linked_list_4))
print(intersection(linked_list_3, linked_list_4))
