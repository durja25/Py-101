# This is an example of a lambda function
add_4 = lambda x: x + 4
# This argument is inserted into the variable found in the lambda function
print(add_4(4))

# We can have two or more paramters in lambda as well
add = lambda x, y: x + y
print(add(10, 4))


# This is equivalent to the "add" lambda function
def addf(x, y):
    return x + y


print(addf(10, 4))

# We can create, evaluate and print a lambda function all in one line.
print((lambda x, y: x + y)(10, 4))

is_even = lambda x: x % 2 == 0
# We can easily see if a number is even or odd using lambda functions. we can see this being useful.
print(is_even(2))
print(is_even(3))

# We can use lambdas to iterate. I need to further
# inspect this statement
blocks = lambda x, y: [x[i:i + y] for i in range(0, len(x), y)]
print(blocks("string", 2))

# This can help put the elements in order for strings
to_ord = lambda x: [ord(i) for i in x]
print(to_ord("ABCD"))


# This is just the "to_ord" lambda written in a normal function.
def to_ord2(x):
    ret = []
    for i in x:
        ret.append(ord(i))
    return ret


print(to_ord2("ABCD"))