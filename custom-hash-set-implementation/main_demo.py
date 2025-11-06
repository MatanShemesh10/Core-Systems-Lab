from custom_set import MySet

def main():
    print("=== MySet Demonstration ===\n")

    # Create sets
    s1 = MySet([1, 2, 3, 4])
    s2 = MySet([3, 4, 5, 6])

    print("Initial sets:")
    print("s1 =", s1)
    print("s2 =", s2)
    print()

    # Add and remove operations
    print("Adding and removing elements:")
    s1.add(10)
    print("After s1.add(10):", s1)
    s1.remove(2)
    print("After s1.remove(2):", s1)
    print()

    # Membership test
    print("Membership check:")
    print("Is 3 in s1?", 3 in s1)
    print("Is 2 in s1?", 2 in s1)
    print()

    # Mathematical operations
    print("Union:", s1.union(s2))
    print("Intersection:", s1.intersection(s2))
    print("Difference (s1 - s2):", s1.difference(s2))
    print("Symmetric difference:", s1.symmetric_difference(s2))
    print()

    # Operator overloads
    print("Operator overload examples:")
    print("s1 | s2 =", s1 | s2)
    print("s1 & s2 =", s1 & s2)
    print("s1 - s2 =", s1 - s2)
    print("s1 ^ s2 =", s1 ^ s2)
    print()

    # Set relationship checks
    print("Subset / Superset checks:")
    s3 = MySet([3, 4])
    print("s3 =", s3)
    print("s3 ⊆ s1?", s3.issubset(s1))
    print("s1 ⊇ s3?", s1.issuperset(s3))
    print("s1 and s2 disjoint?", s1.isdisjoint(s2))
    print()

    # Copy and equality
    print("Copy and equality test:")
    s4 = s1.copy()
    print("s4 (copy of s1):", s4)
    print("s1 == s4 ?", s1 == s4)
    print()

    # Clear
    print("Clearing s1:")
    s1.clear()
    print("s1 after clear:", s1)
    print()

    print("=== End of Demonstration ===")


if __name__ == "__main__":
    main()
