from collections import OrderedDict

class LRUCache:
    # Constructor for initializing the cache capacity with the given value.
    def __init__(self, cap):
        self.cache = OrderedDict()  # OrderedDict maintains insertion order
        self.capacity = cap         # Capacity of the cache

    # Function to return the value corresponding to the key.
    def get(self, key):
        if key in self.cache:
            # Move the accessed key to the end to mark it as recently used
            value = self.cache.pop(key)
            self.cache[key] = value
            return value
        else:
            return -1  # Key not found in cache

    # Function for storing key-value pair.
    def put(self, key, value):
        if key in self.cache:
            # Key exists, remove it to update its position later
            self.cache.pop(key)
        elif len(self.cache) >= self.capacity:
            # Cache is at full capacity, remove the least recently used item
            self.cache.popitem(last=False)
        # Add the new key-value pair
        self.cache[key] = value
