class CacheLevel:
    def __init__(self, size, eviction_policy):
        self.size = size
        self.eviction_policy = eviction_policy
        self.cache = {}
        self.access_order = []  # For LRU
        self.frequency = {}  # For LFU

    def get(self, key):
        if key in self.cache:
            if self.eviction_policy == 'LRU':
                self.access_order.remove(key)
                self.access_order.append(key)
            elif self.eviction_policy == 'LFU':
                self.frequency[key] += 1
            return self.cache[key]
        return None

    def put(self, key, value):
        if len(self.cache) >= self.size:
            self.evict()
        self.cache[key] = value
        if self.eviction_policy == 'LRU':
            self.access_order.append(key)
        elif self.eviction_policy == 'LFU':
            self.frequency[key] = 1

    def evict(self):
        if self.eviction_policy == 'LRU':
            oldest = self.access_order.pop(0)
            del self.cache[oldest]
        elif self.eviction_policy == 'LFU':
            least_frequent = min(self.frequency, key=self.frequency.get)
            del self.cache[least_frequent]
            del self.frequency[least_frequent]

class CacheManager:
    def __init__(self):
        self.levels = []

    def addCacheLevel(self, size, eviction_policy):
        self.levels.append(CacheLevel(size, eviction_policy))

    def get(self, key):
        for level in self.levels:
            value = level.get(key)
            if value is not None:
                self.promote(key, value)
                return value
        return None

    def put(self, key, value):
        if self.levels:
            self.levels[0].put(key, value)

    def promote(self, key, value):
        for i in range(len(self.levels) - 1, 0, -1):
            if key in self.levels[i].cache:
                self.levels[i].cache.pop(key)
                self.levels[i-1].put(key, value)

    def removeCacheLevel(self, level):
        if 0 <= level < len(self.levels):
            del self.levels[level]

    def displayCache(self):
        for i, level in enumerate(self.levels):
            print(f"L{i+1} Cache: {level.cache}")

# Example usage
cache_manager = CacheManager()
cache_manager.addCacheLevel(3, 'LRU')
cache_manager.addCacheLevel(2, 'LFU')
cache_manager.put("A", "1")
cache_manager.put("B", "2")
cache_manager.put("C", "3")
print(cache_manager.get("A"))
cache_manager.put("D", "4")
print(cache_manager.get("C"))
cache_manager.displayCache()
