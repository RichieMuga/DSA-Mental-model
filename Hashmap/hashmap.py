class HashMap:
    def __init__(self, capacity=10):
        # Initialize with a fixed number of buckets
        self.capacity = capacity
        self.size = 0
        self.buckets = [[] for _ in range(capacity)]  # list of lists (chaining)

    def _hash(self, key):
        """Hash function to get index for a key."""
        return hash(key) % self.capacity

    def put(self, key, value):
        """Insert or update a key-value pair."""
        index = self._hash(key)
        bucket = self.buckets[index]

        # Check if key already exists and update
        for i, (k, v) in enumerate(bucket):
            if k == key:
                bucket[i] = (key, value)
                return

        # Otherwise, insert new key-value pair
        bucket.append((key, value))
        self.size += 1

        # Optional: resize if load factor too high
        if self.size / self.capacity > 0.7:
            self._resize()

    def get(self, key):
        """Retrieve value for a key, or None if not found."""
        index = self._hash(key)
        bucket = self.buckets[index]

        for k, v in bucket:
            if k == key:
                return v
        return None

    def remove(self, key):
        """Remove key-value pair by key."""
        index = self._hash(key)
        bucket = self.buckets[index]

        for i, (k, v) in enumerate(bucket):
            if k == key:
                del bucket[i]
                self.size -= 1
                return True
        return False

    def _resize(self):
        """Double the capacity and rehash all keys."""
        old_buckets = self.buckets
        self.capacity *= 2
        self.buckets = [[] for _ in range(self.capacity)]
        self.size = 0

        for bucket in old_buckets:
            for k, v in bucket:
                self.put(k, v)

    def __len__(self):
        """Return number of elements."""
        return self.size

    def __repr__(self):
        """Readable format for debugging."""
        items = []
        for bucket in self.buckets:
            for k, v in bucket:
                items.append(f"{k}: {v}")
        return "{" + ", ".join(items) + "}"

h = HashMap()

h.put("name", "Richie")
h.put("age", 25)
h.put("city", "Nairobi")

print(h.get("name"))   
print(h.get("age"))       

h.put("age", 26)          
print(h.get("age"))       

h.remove("city")
print(h.get("city"))      

print(h)                 
print(len(h))             
