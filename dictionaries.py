# dictionary - used for store data in key value pairs and can not have duplicates keys


# This is how you declare a dictionary
dict1 = {"a": 1, "b": 2, "c": 3}
print(dict1)
print(type(dict1))
print(len(dict1))

# We put the key instead of an index then Python will print out the value
print(dict1["a"])
# This is another way we can call a value by entering the key
print(dict1.get("a"))

# This prints all the keys in the dictionary
print(dict1.keys())
# This prints all the values in the dictionary
print(dict1.values())
# This prints out all the dictionary in tuple form
print(dict1.items())

# We can't add duplicates. There will be no changes here.
dict1["a"] = 1
print(dict1)

# We can add the another key value pair in a dictionary
dict1["d"] = 4
print(dict1)

# We can change the value of a key using this method
dict1["a"] = 0
print(dict1)

# This is another way we can change
dict1.update({"a": 1})
print(dict1)

# By entering the key here, it removes the key value pair from the dictionary.  By default,
# it removes the last key value pair of the dictionary if a key is not inserted in the input
dict1.pop("d")
print(dict1)

# This is another way we can delete a key value pair from the dictionary
del dict1['c']
print(dict1)

# We can create nested dictionaries. Values can be whole new dictionaries.
dict1['c'] = {"a": 1, "b": 2}
print(dict1)

# We can also create empty dictionaries
dict2 = {}
print(dict2)

# This is another way we can create dictionaries
dict3 = dict()
print(dict3)

# Creating dictionary from list
a = ['st', 'ri', 'ng']

print(dict(enumerate(a)))


# changing dict to list using zip function
dict1 = {"a": 1, "b": 2, "c": 3}

print(list(zip(*dict1)))

# turning two lists into dictionary
a = ['a', 'b', 'c', 'd' ]
b = [10 ,20 , 13, 18]

# a first as an key and b as value
di = dict(zip(a,b))

# b first as an key and a as value
di = dict(zip(b,a))

print(di)



# merging dictionaries using update function
dict1 = {"a": 1, "b": 2, "c": 3}
dict2 = {"city": "Kolkata","country": "India"}

dict1.update(dict2)

# merging dictionaries using ** operator

one = {**dict1,**dict2}

# merging dictionaries using | union operator

one = dict1 | dict2
print(one)


# get method in dict
# default value if key is not there is 0
counts = { 'quincy' : 1 , 'mrugesh' : 42, 'beau': 100, '0': 10}
print(counts.get('kris', 0))