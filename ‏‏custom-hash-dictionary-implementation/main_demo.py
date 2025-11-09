from custom_dictionary import MyDict

def main():
    print("=== MyDict Demonstration ===\n")

    # Create dictionaries
    d1 = MyDict({"a": 1, "b": 2, "c": 3})
    d2 = MyDict({"b": 20, "d": 4})

    print("Initial dictionaries:")
    print("d1 =", d1)
    print("d2 =", d2)
    print()

    # Add and update elements
    print("Adding and updating elements:")
    d1["x"] = 99
    print("After d1['x'] = 99:", d1)
    d1["b"] = 200
    print("After updating d1['b'] = 200:", d1)
    print()

    # Access and membership
    print("Access and membership:")
    print("d1['a'] =", d1["a"])
    print("Is 'c' in d1?", "c" in d1)
    print("Is 'z' in d1?", "z" in d1)
    print()

    # Iteration examples
    print("Iteration examples:")
    print("Keys:", list(d1.keys()))
    print("Values:", list(d1.values()))
    print("Items:", list(d1.items()))
    print()

    # Remove and pop
    print("Removing and popping elements:")
    d1.discard("x")
    print("After d1.discard('x'):", d1)
    removed = d1.pop("a")
    print(f"After d1.pop('a') -> returned {removed}:", d1)
    print()

    # Update from another dict
    print("Updating from another dict:")
    d1.update(d2)
    print("After d1.update(d2):", d1)
    print()

    # Copy and equality
    print("Copy and equality test:")
    d3 = d1.copy()
    print("d3 (copy of d1):", d3)
    print("d1 == d3 ?", d1 == d3)
    print()

    # Clear
    print("Clearing d1:")
    d1.clear()
    print("d1 after clear:", d1)
    print()

    print("=== End of Demonstration ===")


if __name__ == "__main__":
    main()
