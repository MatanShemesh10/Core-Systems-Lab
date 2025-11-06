import time
import random
from custom_set import MySet

def benchmark():

    # Number of elements for testing
    N = 200_000
    keys = [random.randint(0, N * 5) for _ in range(N)]

    # Create both sets
    myset = MySet()
    realset = set()

    # ---------- ADD TEST ----------
    print("Add operation benchmark:")

    start = time.perf_counter()
    for k in keys:
        myset.add(k)
    my_time_add = time.perf_counter() - start

    start = time.perf_counter()
    for k in keys:
        realset.add(k)
    real_time_add = time.perf_counter() - start

    # ---------- SEARCH TEST ----------
    print("Search operation benchmark:")

    test_keys = random.sample(keys, 10_000)

    start = time.perf_counter()
    for k in test_keys:
        _ = k in myset
    my_time_find = time.perf_counter() - start

    start = time.perf_counter()
    for k in test_keys:
        _ = k in realset
    real_time_find = time.perf_counter() - start

    # ---------- REMOVE TEST ----------
    print("Remove operation benchmark:")

    start = time.perf_counter()
    for k in test_keys:
        myset.discard(k)
    my_time_remove = time.perf_counter() - start

    start = time.perf_counter()
    for k in test_keys:
        realset.discard(k)
    real_time_remove = time.perf_counter() - start

    # ---------- SUMMARY ----------
    print("\n========== Benchmark Results ==========")
    print(f"Add:    MySet = {my_time_add:.4f}s | Built-in set = {real_time_add:.4f}s")
    print(f"Search: MySet = {my_time_find:.4f}s | Built-in set = {real_time_find:.4f}s")
    print(f"Remove: MySet = {my_time_remove:.4f}s | Built-in set = {real_time_remove:.4f}s")

    print("\nRelative performance (MySet / set):")
    print(f"Add:    {my_time_add / real_time_add:.2f}x slower")
    print(f"Search: {my_time_find / real_time_find:.2f}x slower")
    print(f"Remove: {my_time_remove / real_time_remove:.2f}x slower")

if __name__ == "__main__":
    benchmark()