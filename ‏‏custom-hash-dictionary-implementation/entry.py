class Entry():
    def __init__(self, key, value, hash_):
        self._key = key
        self._value = value
        self._hash = hash_

    def __repr__(self):
        return str(self._key)
    
class _Deleted():
    def __repr__(self):
        return "DELETED"