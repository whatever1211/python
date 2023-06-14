class HashTable:
    def __init__(self, size):
        self.size = size
        self.hash_table = self.create_buckets()
 
    def create_buckets(self):
        return {}
 
    def set_val(self, key, val):
        hashed_key = hash(key) % self.size
        bucket = self.hash_table.get(hashed_key)
        if bucket:
            found_key = False
            for index, record in enumerate(bucket):
                record_key, record_val = record
                if record_key == key:
                    found_key = True
                    break
            if found_key:
                bucket[index] = (key, val)
            else:
                bucket.append((key, val))
        else:
            self.hash_table[hashed_key] = []
            self.hash_table[hashed_key].append((key, val))
 
    def get_val(self, key):
        hashed_key = hash(key) % self.size
        bucket = self.hash_table.get(hashed_key)
        if bucket:
            found_key = False
            for index, record in enumerate(bucket):
                record_key, record_val = record
                if record_key == key:
                    found_key = True
                    break
            if found_key:
                return record_val
            else:
                return None
        else:
            return None
 
    def delete_val(self, key):
        hashed_key = hash(key) % self.size
        bucket = self.hash_table.get(hashed_key)
        if bucket:
            found_key = False
            for index, record in enumerate(bucket):
                record_key, record_val = record
                if record_key == key:
                    found_key = True
                    break
            if found_key:
                bucket.pop(index)
    def __str__(self):
        return "\n".join(str(item) + " " + str(self.hash_table[item]) for item in self.hash_table)

gridHashTable = HashTable(pow(10, 9) + 7)
gridHashTable.set_val("KEY", "VALUE")
gridHashTable.get_val("KEY")
gridHashTable.delete_val("KEY")
print(str(gridHashTable))
