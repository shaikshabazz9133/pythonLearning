# SET:
# A set is an unordered collection of unique and immutable items. Duplicate elements are automatically removed.
# 1. Creating Sets
mySet = {1, 2, 3, 4, 5}
anotherSet = {4, 5, 6, 7, 8}
print(f"Initial Set: {mySet}")

# 2. Adding and Removing Elements
mySet.add(6)  # Adds an element
print(f"After add(6): {mySet}")

mySet.remove(2)  # Removes an element (raises error if not found)
print(f"After remove(2): {mySet}")

mySet.discard(10)  # Removes an element safely (no error if not found)
print(f"After discard(10): {mySet}")

# 3. Set Operations (Math Operations)
# Union: Combines both sets (all unique elements)
unionSet = mySet | anotherSet
print(f"Union (|): {unionSet}")

# Intersection: Elements common to both sets
intersectionSet = mySet & anotherSet
print(f"Intersection (&): {intersectionSet}")

# Difference: Elements in mySet but not in anotherSet
differenceSet = mySet - anotherSet
print(f"Difference (-): {differenceSet}")

# Symmetric Difference: Elements in either set, but not in both
symDiffSet = mySet ^ anotherSet
print(f"Symmetric Difference (^): {symDiffSet}")

# 4. Subset and Superset Checks
subSet = {3, 4}
print(f"Is 'subSet' a subset of mySet?: {subSet.issubset(mySet)}")
print(f"Is mySet a superset of 'subSet'?: {mySet.issuperset(subSet)}")
