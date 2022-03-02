num = [2, 8, 12, 18, 54, 65, 87,88]

def square(x):
    return x*x

# maps takes in a function and iterable list and gives result but we have to typecast it because its returns object
new = map(square, num)

# we can also use it to type cast list into str type
# it works with any function inside or outside
new = map(str, num)
print(list(new))

# filter returns the items
numbers = [1,2,3,4,5,6,7,8,9,10]
filter_list = list(filter(lambda x : (x % 2 == 0),numbers))
print(f'Filtered list : {filter_list}')

# Whereas map returns all the items in the list returned by the specified function.
# Here, all the even numbers are returned as True and remaining as False by map function.

map_list = list(map(lambda x : (x % 2 == 0),numbers))
print(f'Mapped list : {map_list}')


# Zip is a container that hold the data inside.
# zip function takes iterable elements as input, and returns iterator.
list1 = ['Alpha', 'Beta', 'Gamma', 'Sigma']
list2 = ['one', 'two', 'three', 'six']

test = zip(list1, list2)  # zip the values

print('\nPrinting the values of zip')
for values in test:
    print(values)  # print each tuples











from functools import reduce
numbers = [1,2,3,4]
# reduce requires two parameters, it assigns 1 and 2 as x and y initially
reduced_number = reduce(lambda x,y: x*y, numbers)
print(reduced_number)
# 1 2  3   4
# \/  /   /
# 2  /   /
#  6    /
#    24