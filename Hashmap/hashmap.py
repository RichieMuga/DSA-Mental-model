class Hashmap:
    def __init__(self):
        self.capacity = 9
        self.buckets = [[] for _ in range(len(self.capacity))]
        self.size = 0
    
    def _hash(self, key):
        return hash(key) % self.capacity
    
    def put(self, key, value):
        index = self._hash(key)
        bucket = self.buckets[index]

        for i (k,v) in enumerate(bucket): # type: ignore
            if k == key: # type: ignore
                bucket[i] = (key,value) # type: ignore
                return
        
        bucket.append((key,value))

        self.size+=1
    
    def get(self, key):
        index = self._hash(key)
        bucket = self.buckets[index]

        for k, v in bucket:
            if k == key:
                return v
        return None

    def remove(self, key):
        index = self._hash(key)
        bucket = self.buckets[index]

        for i, (k, v) in enumerate(bucket):
            if k == key:
                del bucket[i]
                self.size -= 1
                return True
        return False