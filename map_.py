num = [2, 8, 12, 18, 54, 65, 87,88]

def square(x):
    return x*x

# maps takes in a function and iterable list and gives result but we have to typecast it because its returns object
new = map(square, num)

# we can also use it to type cast list into str type
# it works with any function inside or outside
new = map(str, num)
print(list(new))