import time
import random
from custom_dictionary import MyDict

def benchmark():

    N = 200_000
    keys = [random.randint(0, N * 5) for _ in range(N)]
    values = [random.randint(0, 10_000) for _ in range(N)]

    mydict = MyDict()
    realdict = {}

    # ---------- ADD TEST ----------
    print("Add operation benchmark:")

    start = time.perf_counter()
    for k, v in zip(keys, values):
        mydict[k] = v
    my_time_add = time.perf_counter() - start

    start = time.perf_counter()
    for k, v in zip(keys, values):
        realdict[k] = v
    real_time_add = time.perf_counter() - start

    # ---------- SEARCH TEST ----------
    print("Search operation benchmark:")

    test_keys = random.sample(keys, 10_000)

    start = time.perf_counter()
    for k in test_keys:
        _ = k in mydict
    my_time_find = time.perf_counter() - start

    start = time.perf_counter()
    for k in test_keys:
        _ = k in realdict
    real_time_find = time.perf_counter() - start

    # ---------- REMOVE TEST ----------
    print("Remove operation benchmark:")

    start = time.perf_counter()
    for k in test_keys:
        mydict.discard(k)
    my_time_remove = time.perf_counter() - start

    start = time.perf_counter()
    for k in test_keys:
        realdict.pop(k, None)
    real_time_remove = time.perf_counter() - start

    # ---------- SUMMARY ----------
    print("\n========== Benchmark Results ==========")
    print(f"Add:    MyDict = {my_time_add:.4f}s | Built-in dict = {real_time_add:.4f}s")
    print(f"Search: MyDict = {my_time_find:.4f}s | Built-in dict = {real_time_find:.4f}s")
    print(f"Remove: MyDict = {my_time_remove:.4f}s | Built-in dict = {real_time_remove:.4f}s")

    print("\nRelative performance (MyDict / dict):")
    print(f"Add:    {my_time_add / real_time_add:.2f}x slower")
    print(f"Search: {my_time_find / real_time_find:.2f}x slower")
    print(f"Remove: {my_time_remove / real_time_remove:.2f}x slower")


if __name__ == "__main__":
    benchmark()