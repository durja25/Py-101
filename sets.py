# set - can store multiple values in one var, sets can not be ordered and do not allow duplicates

set1 = {"a", "b", "c"}
# When it's printed, the elements of the set are printed randomly
print(set1)
print(type(set1))

# duplicate values are counted as only one value
set2 = {"a", "a", "a"}
print(set2)
print(len(set2))

# We can have different data types as elements of sets
set3 = {"a", 0, True}
print(set3)

# This is another way of declaring a set
set4 = set(("b", 1, False))
print(set4)

# We can add an element to a set
set1.add("d")
print(set1)

# This combines the elements
set3.update(set4)
print(set3)

list1 = ["a", "b", "c"]
set4 = {4, 5, 6}
print(list1)
print(set4)

# We can combine lists with sets
set4.update(list1)
print(set4)

set5 = {4, 5, 6}
# This is another way to combine sets
set6 = set4.union(set5)

# We can remove an element from sets using the remove function
set4.remove(4)
print(set4)

# This won't bring up an error even if the element is not there but will remove it if it is in the set
set4.discard(4)
print(set4)

print(set1)
# This will pop a random element since sets are not ordered.
set1.pop()
print(set1)