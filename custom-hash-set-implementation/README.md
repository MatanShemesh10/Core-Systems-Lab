# Custom Set Implementation (`MySet`)

This project is a custom implementation of a **hash-based set data structure** in Python, featuring linear probing, dynamic resizing, and lazy deletion.

It replicates the behavior of Python's built-in `set`, while exposing the underlying logic of hash tables for educational and performance exploration.

---

## Project Structure

```
custom-set/
├── entry.py              # Contains Entry and _Deleted classes
├── custom_set.py         # Full implementation of the MySet data structure
├── main_demo.py          # Demonstration of usage and available operations
└── main_benchmark.py     # Performance benchmark vs Python's built-in set
```

---

## Features

* Hash table with **linear probing** for collision resolution
* **Dynamic resizing** when load factor exceeds 0.66
* **Lazy deletion** using a special DELETED marker
* Full support for set operations:

  * `union`, `intersection`, `difference`, `symmetric_difference`
  * `issubset`, `issuperset`, `isdisjoint`
  * Operator overloads: `|`, `&`, `-`, `^`
* Includes a **copy method**, equality check, and iterator support

---

## Usage Example

```python
from custom_set import MySet

s1 = MySet([1, 2, 3])
s2 = MySet([3, 4, 5])

print("s1 | s2 =", s1 | s2)
print("s1 & s2 =", s1 & s2)
print("s1 - s2 =", s1 - s2)
```

Run `main_demo.py` for a full demonstration of all operations.

---

## Benchmark

Run the benchmark file to compare performance against Python's built-in `set`:

```bash
python main_benchmark.py
```

Example output (on 200K elements):

```
========== Benchmark Results ==========
Add:    MySet = 0.8340s | Built-in set = 0.0219s
Search: MySet = 0.0093s | Built-in set = 0.0012s
Remove: MySet = 0.0149s | Built-in set = 0.0075s
```

While slower due to Python-level execution, the results demonstrate the same **O(1) average time complexity** for all operations.

---

## Author

Developed by Matan Shemesh as part of the **core-systems-lab** repository - a personal lab for exploring system-level and data-structure engineering in Python and C++.
