# tuple - data is fixed then it is good for use. Its immutable.

# We declare tuples this way
tuple_items = ("item1", "item2", "item3")
print(tuple_items)
print(type(tuple_items))

tuple_numbers = (1, 2, 3)
print(tuple_numbers)
print(type(tuple_numbers))

# We can also write tuples this way
# multiply
tuple_repeat = ('Combine!',) * 4
print(tuple_repeat)
print(type(tuple_repeat))

# A tuple can have different types of items in it
# including a nested tuple
tuple_mixed = ("A", 1, ("A", 1))
print(tuple_mixed)
print(type(tuple_mixed))

# we can not add to tuple but we can join 2 tuple together
tuple_combined = tuple_items + tuple_numbers
print(tuple_combined)
print(type(tuple_combined))


# This is a way we can unpack tuples
item1, item2, item3 = tuple_items
print(item1)
print(item2)
print(item3)

# Check if a string or any item is in a tuple
print("item2" in tuple_items)
print("item4" in tuple_items)

# Gives us the index number of an item.
# it will give us -1 if it doesn't exist
print(tuple_items.index("item2"))

# Prints the item that is in the indicated index number of the tuple
print(tuple_items[0])

# Prints the length of a tuple
print(len(tuple_items))

# This is the last item that's getting printed. negative numbers means counting backwards
print(tuple_items[-1])

# We can print parts of the tuple using these index numbers. The last index number won't be
print(tuple_items[0:2])
# included in the print.
# Same concept with the index number starting from 0
print(tuple_items[:2])

# We can count the index numbers backwards
print(tuple_items[-3:-1])




string1 = "I am a string!"
# The concept of indexes also applies with strings
print(string1[0:4])
print(string1[:-1])