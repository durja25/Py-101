# list - we can change data, they r ordered and allow duplicates

# This is how we can declare a list
list1 = ["A", "B", "C", "D", "E", "F"]
print(list1)

# A list can contain different data types including a nested
list2 = ["A", 1, 2.0, ["A"], [], list(), ("A"), False]

print(list2)
print(type(list2))

# We can use indexing to print specific elements of the list
print(list1[0])
print(list1[-1])
# Here we are asking to get into the nested list on the 3rd index then print the first element in
print(list2[3][0])

# We can do the same thing while counting backwards
print(list2[3][-1])

# changing contents of the list using this syntax
list1[0] = "X"
print(list1)

# We can also delete contents of the list using this syntax
del list1[0]
print(list1)

# We can insert an element by first showing the index number we want it on and then inserting
# the element
list1.insert(0, "A")
print(list1)

del list1[0]
print(list1)

list1 = ["A"] + list1  # This is another way we can insert elements. This adds it to the front of the list
print(list1)

# Another way to insert elements.
# This adds it on the end/last position of the list.
list1.append("G")
print(list1)

# It will let us know the maximum value in the list.
print(max(list1))
# It will let us know the minimum value in the list.
print(min(list1))

# We can find out the index of an element using this syntax. Python will return -1 if the
# element is not found in the list.
print(list1.index("C"))
# This is a nested expression where list1 gets the index of an element as an input,
# then it will spit out the element in return.
print(list1[list1.index("C")])


# Reverses the order of the whole list
list1.reverse()
print(list1)


# This is another way to reverse the list
list1 = list1[::-1]
# syntactic sugar
# [START:STOP:STEP]
print(list1)

# This counts the number of times the element in the input appears in the list
print(list1.count("A"))
list1.append("A")
print(list1)
print(list1.count("A"))

# This removes the last element of the list
list1.pop()
print(list1)

list3 = ["H", "I", "J"]
print(list3)

# This adds the list in the input to the list the function is being used on.
list1.extend(list3)
print(list1)

# This deletes every element in the list and it becomes an empty list
list1.clear()
print(list1)

list4 = [8, 12, 5, 6, 17, 2]
print(list4)

# We can sort the list in increasing order using the sort function
list4.sort()
print(list4)

# We can sort the list in decreasing order using the sort function
list4.sort(reverse=True)
print(list4)

# This is a reference only to list4 and not an actual copy
list5 = list4
print(list4)
print(list5)

# This will modify both list4 and list5
list5[2] = "X"
print(list5)
print(list4)

# This is a legitimate copy of list4 and can be modified without modifying list4
list6 = list4.copy()
print(list4)
print(list6)

# This only modifies list6 and not list4
list6[2] = "A"
print(list6)
print(list4)

list7 = ["1", "2", "3"]
print(list7)

# This would map each element of list7
# and turn it into a float
# (as long as it's applicable)
list8 = list(map(float, list7))
print(list8)

# Combining two values
a = ['a', 'c', 'd','b' ]
b = [10 ,20 , 13, 18]

print(list(zip(a,b)))

# Combining two values and sorting them but keeping both same
# both separete but considering it as connected
a = ['a', 'b', 'c', 'd' ]
b = [10 ,20 , 13, 18]

print(sorted((zip(a,b))))

# print as collection with for loop
a = ['a', 'c', 'd', 'b' ]
b = [10 ,20 , 13, 18]

for i,name in zip(b,a):
    print(f"{name} is of age {i}")

# unzip
a = [('a', 10), ('c', 20), ('d', 13), ('b', 18)]


name,age = zip(*a)

print(list(name))
print(list(age))