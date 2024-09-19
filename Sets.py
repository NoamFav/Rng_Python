# Define two sets
set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}

# Print initial sets
print("Set1:", set1)
print("Set2:", set2)

# Add an element to set1
set1.add(6)
print("After adding 6 to Set1:", set1)

# Remove an element from set2 (safe removal with discard)
set2.discard(8)
print("After discarding 8 from Set2:", set2)

# Union of set1 and set2
union_set = set1.union(set2)
print("Union of Set1 and Set2:", union_set)

# Intersection of set1 and set2
intersection_set = set1.intersection(set2)
print("Intersection of Set1 and Set2:", intersection_set)

# Difference of set1 and set2
difference_set = set1.difference(set2)
print("Difference of Set1 and Set2:", difference_set)

# Symmetric difference of set1 and set2
symmetric_difference_set = set1.symmetric_difference(set2)
print("Symmetric Difference of Set1 and Set2:", symmetric_difference_set)

# Check if an element is in set1
print("Is 3 in Set1?", 3 in set1)

# Check if set1 is a subset of union_set
print("Is Set1 a subset of its union with Set2?", set1.issubset(union_set))

# Check if union_set is a superset of set1
print("Is the union of Set1 and Set2 a superset of Set1?", union_set.issuperset(set1))
