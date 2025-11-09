# Custom Dictionary Implementation (`MyDict`)

This project is a custom implementation of a **hash-based dictionary data structure** in Python, featuring linear probing, dynamic resizing, and lazy deletion.

It replicates the core behavior of Python's built-in `dict`, while exposing the internal mechanics of hash tables - providing a clear, educational look into how key-value stores work under the hood.

---

## Project Structure

```
custom-dict/
├── entry.py              # Contains Entry and _Deleted classes
├── custom_dictionary.py        # Full implementation of the MyDict data structure
├── main_demo.py          # Demonstration of usage and available operations
└── main_benchmark.py     # Performance benchmark vs Python's built-in dict
```

---

## Features

* Hash table with **linear probing** for collision resolution  
* **Dynamic resizing** when load factor exceeds 0.66  
* **Lazy deletion** via a dedicated `_Deleted` marker  
* Full support for common dictionary behaviors:
  * `__getitem__`, `__setitem__`, `__delitem__`, `__contains__`
  * Iteration over `keys()`, `values()`, and `items()`
  * `update`, `get`, `pop`, `discard`, `clear`, `copy`, and equality check  
* Proper **`__repr__` output** for a native Python `dict`-like appearance

---

## Usage Example

```python
from custom_dict import MyDict

d = MyDict({"a": 1, "b": 2})
d["c"] = 3

print("Initial:", d)
print("Keys:", list(d.keys()))
print("Values:", list(d.values()))
print("Items:", list(d.items()))

d.pop("b")
print("After pop:", d)
```

Run `main_demo.py` for a full demonstration of all supported operations.

---

## Benchmark

Run the benchmark file to compare performance against Python’s built-in `dict`:

```bash
python main_benchmark.py
```

Example output (on 200K elements):

```
========== Benchmark Results ==========
Add:    MyDict = 0.9515s | Built-in dict = 0.0409s
Search: MyDict = 0.0086s | Built-in dict = 0.0019s
Remove: MyDict = 0.0124s | Built-in dict = 0.0049s
```

While naturally slower due to Python-level implementation,  
`MyDict` exhibits the same **O(1)** average complexity as a standard dictionary,  
clearly illustrating how hash tables operate in practice.

---

## Author

Developed by **Matan Shemesh** as part of the  
**core-systems-lab** repository - a personal lab for exploring system-level and data-structure engineering in Python and C++.
