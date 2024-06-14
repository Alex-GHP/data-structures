class HashMap:
    def __init__(self, size=8):
        self.hashmap = [None for i in range(size)]

    def key_to_index(self, key):
        sum = 0
        for c in key:
            sum += ord(c)
        return sum % len(self.hashmap)

    def insert(self, key, value):
        self.resize()
        self.hashmap[self.key_to_index(key)] = (key, value)

    def get(self, key):
        try:
            return self.hashmap[self.key_to_index(key)][1]
        except:
            raise Exception("Key not found")
    
    def resize(self):
        if len(self.hashmap) == 0:
            self.hashmap = [None]
            return
        if self.current_load() < 0.05:
            return
        old_hashmap = self.hashmap
        self.hashmap = [None] * (len(old_hashmap) * 10)
        for kvp in old_hashmap:
            if kvp is not None:
                self.insert(kvp[0], kvp[1])
            
    def current_load(self):
        if len(self.hashmap) == 0:
            return 1
        items = 0
        for item in self.hashmap:
            if item is not None:
                items += 1
        return items / len(self.hashmap)
