from collections import deque


class LRU_Cache(object):

    def __init__(self, capacity):

        if capacity < 1:
            raise ValueError('Cache size must be at least 1.')

        self.capacity = capacity
        self.cache = dict()
        self.history = deque()

    def get(self, key):
        # Try to get the key, if it doesn't exist, catch the KeyError and return -1.
        # Note: I'm keeping the size of the history under the capacity.
        # The size of the cache may be smaller if there are repeated gets/puts for the same key.
        try:
            value = self.cache[key]
            self.history.appendleft(key)  # Add to history
            if len(self.history) > self.capacity:  # Manage size of history and sync cache
                self.manage_history_size()
            return value
        except KeyError:  # Key was not present in the cache.
            return -1

    def set(self, key, value):
        # Set the value if the key is not present in the cache.
        # If the history is at capacity remove the oldest item.
        self.history.appendleft(key)  # Update history. O(1)
        self.cache[key] = value  # Set new value. O(1)

        if len(self.history) > self.capacity:  # Maintain size of cache history
            self.manage_history_size()

    def manage_history_size(self):
        # Since we are managing the size of the history, rather than the size of the cache,
        # there may be items in the history that have already been popped off the cache.
        # Need to ignore KeyErrors on the cache pop.
        popped = self.history.pop()
        try:
            self.cache.pop(popped)
        except KeyError:
            pass

    def check_cache(self):  # Debugs
        print(self.cache)
        print(self.history)
        print('')


# Test 1
our_cache = LRU_Cache(5)
our_cache.set(1, 1)
our_cache.set(2, 2)
our_cache.set(3, 3)
our_cache.set(4, 4)
assert our_cache.get(1) == 1
assert our_cache.get(2) == 2
assert our_cache.get(9) == -1  # Because 9 was never present in the cache
our_cache.set(5, 5)
our_cache.set(6, 6)
assert our_cache.get(3) == -1  # Because 3 has been removed from the cache.


# Test 2
our_cache = LRU_Cache(5)
our_cache.set(12343545, 1)
our_cache.set(564, 1)
our_cache.set(456, 1)
our_cache.set(678, 1)
assert our_cache.get(1) == -1
assert our_cache.get(12343545) == 1
assert our_cache.get(564) == 1
assert our_cache.get(678) == 1
our_cache.set(1, 564)
our_cache.set(1, 456)
our_cache.set(1, 678)
assert our_cache.get(1) == 678

print('Tests passed')
