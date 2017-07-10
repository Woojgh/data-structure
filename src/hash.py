class HashTable:

    def __init__(self):
        self.size = 753
        self.slots = [None] * self.size
        self.data = [None] * self.size

    def hashingtons(self, key, size):
        return key % size

    def hashemagain(self, oldcountrystylehash, size):
        return (oldcountrystylehash+1) % size

    def set(self, key, val):
        hash_val = self.hashingtons(key, len(self.slots))

    def get(self, key):
        startingslot = self.hashingtons(key, len(self.slots))

        val = None
        stop = False
        start = False
        position = startingslot
