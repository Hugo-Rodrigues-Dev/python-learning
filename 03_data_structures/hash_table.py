class HashTable:
    def __init__(self, capacity=16, load_factor=0.75):
        if capacity <= 0:
            raise ValueError("capacity must be positive")
        self._capacity = capacity
        self._buckets = [[] for _ in range(capacity)]
        self._size = 0
        self._load_factor = load_factor

    def _bucket_index(self, key):
        return hash(key) % self._capacity

    def _resize(self):
        old_buckets = self._buckets
        self._capacity *= 2
        self._buckets = [[] for _ in range(self._capacity)]
        self._size = 0
        for bucket in old_buckets:
            for key, value in bucket:
                self[key] = value

    def __setitem__(self, key, value):
        bucket = self._buckets[self._bucket_index(key)]
        for index, (stored_key, _) in enumerate(bucket):
            if stored_key == key:
                bucket[index] = (key, value)
                return
        bucket.append((key, value))
        self._size += 1
        if self._size / self._capacity > self._load_factor:
            self._resize()

    def __getitem__(self, key):
        bucket = self._buckets[self._bucket_index(key)]
        for stored_key, value in bucket:
            if stored_key == key:
                return value
        raise KeyError(key)

    def __delitem__(self, key):
        bucket = self._buckets[self._bucket_index(key)]
        for index, (stored_key, _) in enumerate(bucket):
            if stored_key == key:
                del bucket[index]
                self._size -= 1
                return
        raise KeyError(key)

    def __contains__(self, key):
        bucket = self._buckets[self._bucket_index(key)]
        return any(stored_key == key for stored_key, _ in bucket)

    def __len__(self):
        return self._size

    def items(self):
        for bucket in self._buckets:
            for key, value in bucket:
                yield key, value

    def keys(self):
        for key, _ in self.items():
            yield key

    def values(self):
        for _, value in self.items():
            yield value


if __name__ == "__main__":
    phone_book = HashTable()
    phone_book["Alice"] = "0695726918"
    phone_book["Bob"] = "0735942919"
    phone_book["Charlie"] = "0697915320"

    print("Entries:")
    for name, number in phone_book.items():
        print(f"- {name}: {number}")

    print("\nLookup Bob:", phone_book["Bob"])

    phone_book["Daisy"] = "0695722158"
    print("Size after adding Daisy:", len(phone_book))
    print("Contains Alice?", "Alice" in phone_book)

    del phone_book["Alice"]
    print("Size after removing Alice:", len(phone_book))
