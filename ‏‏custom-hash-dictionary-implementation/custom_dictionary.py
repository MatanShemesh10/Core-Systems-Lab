from entry import Entry, _Deleted

class MyDict():

    def __init__(self, iterable = None, initial_size = 8):
        self._initial_size = initial_size
        self._table = [None] * self._initial_size
        self._capacity = self._initial_size 
        self._size = 0 # actual number of entries inside the table
        self._DELETED = _Deleted()
        if iterable:
            self.update(iterable)
    
    def resize(self):
        self._capacity *= 2
        old_table = self._table
        self._table = [None] * (self._capacity)
        self._size = 0

        for item in old_table:
            if isinstance(item, Entry):
                self.add(item._key, item._value)
        

    def add(self, key, value):
        if self._size / self._capacity > 0.66:
            self.resize()

        hash_ = hash(key)
        index_ = hash_ % self._capacity

        first_deleted = None
        for step in range(self._capacity):
            idx = (index_ + step) % self._capacity
            slot = self._table[idx]

            if slot is None and first_deleted is None: # insert
                self._table[idx] = Entry(key, value, hash_)
                self._size += 1
                return
            elif slot is self._DELETED and first_deleted is None:
                first_deleted = idx
            elif slot is not None and isinstance(slot, Entry) and slot._key == key: # already inside the table, do noting
                slot._value = value
                return
        
        # not found in table, insert at first deleted
        if first_deleted is None: raise KeyError(f"Error occured while trying to find location for key '{key}'")
        self._table[first_deleted] = Entry(key, value, hash_)
        self._size += 1
        
    def update(self, *iterables):
        for iterable in iterables:
            if isinstance(iterable, MyDict) or isinstance(iterable, dict):
                for k, v in iterable.items():
                    self.add(k, v)

            else: # fallback for list of tuples [(k, v), ...]
                for item in iterable:
                    if isinstance(item, (list, tuple)) and len(item) == 2:
                        self.add(item[0], item[1])


    def find(self, key):
        hash_ = hash(key)
        index_ = hash_ % self._capacity

        for step in range(self._capacity):
            idx = (index_ + step) % self._capacity
            slot = self._table[idx]
            
            if slot is None:
                return None
            if isinstance(slot, Entry) and slot._key == key:
                return idx
        
        return None

    def remove(self, key):
        index = self.find(key)
        if index is not None:
            value = self._table[index]._value
            self._table[index] = self._DELETED
            self._size -= 1
            return value
        else:
            raise KeyError(f"{key} not found in set")
    
    def discard(self, key):
        index = self.find(key)
        if index is not None:
            self._table[index] = self._DELETED
            self._size -= 1

    def clear(self):
        self._table = [None] * self._initial_size
        self._size = 0
    
    ####  Mathematical operations between groups 

    def union(self, *iterables):
        result = self.copy()
        result.update(*iterables)
        return result
    
    def intersection(self, *others):
        result = MyDict()
        for item in self:
            if all(item in other for other in others):
                result.add(item)
        return result

    def difference(self, *others):
        result = MyDict()
        for item in self:
            if not any(item in other for other in others):
                result.add(item)
        return result
    
    def symmetric_difference(self, *others): # A.symmetric_difference(B) = (A - B) ∪ (B - A)
        result = self.copy()
        for other in others:
            result = (result.difference(other)).union(other.difference(result))
        return result
    
    def issubset(self, other):
        return all(item in other for item in self)
    
    def issuperset(self, other):
        return all(other_item in self for other_item in other)
    
    def isdisjoint(self, other):
        return not any(item in other for item in self)

    
    #### Comfort and representation

    def __repr__(self):
        pairs = []
        for slot in self._table:
            if isinstance(slot, Entry):
                pairs.append(f"{repr(slot._key)}: {repr(slot._value)}")
        return "MyDict({" + ", ".join(pairs) + "})"
        
    def __contains__(self,key):
        return self.find(key) is not None
    
    def __len__(self):
        return self._size
    
    def __iter__(self): # for loop
        for slot in self._table:
            if isinstance(slot, Entry):
                yield slot._key
    
    def items(self): # for loop
        for slot in self._table:
            if isinstance(slot, Entry):
                yield [slot._key, slot._value]
    
    def values(self): # for loop
        for slot in self._table:
            if isinstance(slot, Entry):
                yield slot._value

    def keys(self):
        for key in self:
            yield key

    def __setitem__(self, key, value):
        self.add(key, value)
    
    def __getitem__(self, key):
        idx = self.find(key)
        if idx is None:
            raise KeyError(key)
        return self._table[idx]._value
    
    def __delitem__(self, key):
        self.remove(key)

    def get(self, key, default=None):
        return ### TODO
    
    def pop(self, key):
        return self.remove(key)
    
    def get(self, key, default=None):
        idx = self.find(key)
        return self._table[idx]._value if idx is not None else default
        
    def copy(self):
        return MyDict(self)
    
    def __eq__(self, other):
        if not isinstance(other, MyDict):
            return False
        return len(self) == len(other) and all(item in other for item in self)
    
    def __or__(self, other):
        return self.union(other)
    
    def __and__(self, other):
        return self.intersection(other)
    
    def __sub__(self, other):
        return self.difference(other)
    
    def __xor__(self, other):
        return self.symmetric_difference(other)