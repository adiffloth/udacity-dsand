import hashlib
import datetime


class Blockchain:

    def __init__(self, data=None):
        self.head = None
        if data:  # Also create the genesis block if data is provided.
            self.prepend(data)

    def prepend(self, data):
        # Add a new block to the chain.
        # The new block is inserted at the head of the chain.
        # This avoids having to traverse the chain to find the tail for each append.

        # Chain is empty, so just add the new block.
        if self.head is None:
            self.head = Block(data, 0)
            return

        # Create the new block and put it at the head of the chain.
        new_head = Block(data, self.head.hash)
        new_head.previous_block = self.head
        self.head = new_head

    def to_list(self):
        out_list = []
        block = self.head
        while block:
            if block.previous_block:
                prev_data = block.previous_block.data
            else:
                prev_data = 'None'
            out_list.append(block.timestamp.strftime("%H:%M:%S") + ' ' + block.data + ' prev=' + prev_data)
            block = block.previous_block
        return out_list

    def size(self):
        size = 0
        block = self.head
        while block:
            block = block.previous_block
            size += 1
        return size

    def __str__(self):
        return str(self.to_list())


class Block:
    def __init__(self, data, previous_hash):
        self.timestamp = datetime.datetime.utcnow()
        self.data = data
        self.previous_hash = previous_hash
        self.previous_block = None
        self.hash = calc_hash(data)


def calc_hash(data):
    sha = hashlib.sha256()
    hash_str = data.encode('utf-8')
    sha.update(hash_str)
    return sha.hexdigest()


# Test 1 - Blockchain with zero blocks
chain = Blockchain()
print(chain)
assert chain.size() == 0

# Test 2 - Blockchain with a single block, create genesis block and chain at the same time.
chain = Blockchain('Genesis block')
print(chain)
assert chain.size() == 1

# Test 3 - Blockchain with a single block, create empty chain, then add genesis block.
chain = Blockchain()
chain.prepend('Genesis block')
print(chain)
assert chain.size() == 1

# Test 4 - Blockchain with multiple blocks
chain = Blockchain('Genesis block')
num_blocks = 10
for i in range(num_blocks - 1):
    chain.prepend('Block number ' + str(i + 2))
print(chain)
assert chain.size() == num_blocks
