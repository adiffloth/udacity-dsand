## LRU Cache 
I chose to implement this using a hashmap (Python dictionary) and a double ended queue. The dictionary allows me to efficiently store/retrieve the cache keys and values. The deque allows me to efficiently keep track of the history of cache accesses.

An interesting question arises around cache eviction policy - should the capacity apply to the history or the cache itself? The way I implemented this, the capacity applies to the size of the history and it is a true chronological history. I don't check for duplicates in the history, I just enqueue as they come in. This can result in cache dicts that are smaller than the capacity. For example if the capacity is set to 5 and 5 consecutive gets are made for the same key, the history will consist of 5 entries for that same key, and the cache will only have one entry since the other keys will have been evicted as we keep the (non-unique) history to a size of 5.

The advantage of this approach is that managing history remains O(1) since I'm just popping and enqueuing. If the desired behavior is to keep the last 5 **unique** items in history and the corresponding 5 items in the cache, I would have to remove() that particular element from the history, which would require an O(n) traversal of the history deque.

Another approach would be to implement the history as an OrderedDict or even as a plain dict. Both of these maintain insertion order (plain dict since Python 3.6). In the end, I decided to stick with a deque for the history in order to get more experience managing these data structures on my own, rather than relying on higher-level Python constructs.

The time complexity of both get() and set() is O(1). All of the calls inside those functions (eg: in, pop, appendLeft) are O(1), so the overall time complexity is O(1).

The space complexity is controlled by the size of the history. It is O(n). In our tests, we set it arbitrarily to 5.