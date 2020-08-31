## Blockchain

This blockchain is implemented as a linked list where new blocks are added to the head of the list. This way we don't have to traverse the entire chain to find the tail when we add a new block to the chain. This assumes that most of the transactions will be adding blocks rather than accessing the genesis block.

The blocks themselves contain a timestamp, a data attribute, a pointer to the previous block, the previous block's SHA-256 hash and its own SHA-256 hash.

### Time complexity

prepend() is O(1) since it just inserts at the head end.
to_list() and size() are both O(n) since they traverse the entire chain.

### Space complexity

This blockchain is O(n) where n is the number of blocks in the chain.