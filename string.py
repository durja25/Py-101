# python string  are immutable

string1 = "I am a string!"

string2 = 'I am a string too!'

print(string1)
print(string2)


string3 = """I am a long
long
string!"""

print(string3)

string4 = "I\"m a string"
print(string4)

string5 = "I\"m a string\nI\"m on a new line"
print(string5)

string6 = "\\\x41\x42\x43"
print(string6)

string7 = "aaaaaaaaaa"
print(string7)

string7 = "a" * 16
print(string7)

print(len(string7))

# We can check if the string in argument is found in the string variable
print("neut" in string4)
print(string4.startswith("I\"m a"))
print(string4.startswith("n"))
print(string4.endswith("n"))

# the index is the position a part of a string is in inside of a variable
print(string4.index("string"))

# prints the string variable in upper case
print(string4.upper())

# prints the string variable in lower strength
print(string4.lower())

messy_string = "    Messy string!   "
print(messy_string)
# This function strips unnecessary white spaces in a string variable
print(messy_string.strip())

# This function replaces part of a string with another string
print(messy_string.replace("!", "?"))

# You can string two operations together
print(messy_string.replace("!", "?").strip())

# split() converts strings to list
print(messy_string.strip().split())
# By default, split function splits on spaces but we can also specifically
print(messy_string.strip().split("s"))
# tell it
# where to split our string variable


string4 = "I am a string!"
print(string4)
# encode function encodes your string using different formats
print(string4.encode())
print(string4.encode("utf-8"))

# adjusts the string by the specified number starting from the start. Uses space by default.
print(string4.rjust(25))
# does the same thing but instead of using space, uses the given String
print(string4.rjust(25, "X"))

print(string4.ljust(25))
print(string4.ljust(25, "X"))


# This is called concatenation. Python takes these two separates strings and adds
# them up because of the plus sign
print("I am " + " a string")
print("String4 is " + str(len(string4)) + " characters long!")  # We had to cast the length because you can't
# concatenate
# an integer and a string


# This isn't concatenation because these are integers
print(1 + 1)
# This is concatenation because these are strings
print("1" + "1")

# The plus sign is called an overloaded operator because it can do different things.


# We concatenated and casted it automatically using
# the format function
print("string4 is {} characters long!".format(len(string4)))



# Another way to use the format function
print("{} {} {}".format(len(string4), 5.0, 0x12))
# We can use index numbers to determine which comes first
print("{0} {2} {1}".format(len(string4), 5.0, 0x12))

# You can use variables in the format function
print("{length}".format(length=len(string4)))

length = len(string4)
# This is another way we can use the format method
print(f"string4 is {length} characters long")




# The colon and .2f shows the format
# of the file we want to see it in, in this case, it's float numbers with 2 decimal numbers
# .3f means 3 decimal points in a float number. We can use other number system using this same method.
print("string4 is {length:.2f} characters long.".format(length=len(string4)))



print("string4 is {length:x} characters long.".format(length=len(string4)))  # hexadecimal number method
print("string4 is {length:b} characters long.".format(length=len(string4)))  # binary number method
print("string4 is {length:o} characters long.".format(length=len(string4)))  # octal number method
# x represents hexadecimals
# b represents binaries
# o represents octal

print("string4 is %d characters long!" % len(string4))  # %d is a placeholder for numbers
# %s is a placeholder for strings
print("string4 is %x characters long!" % len(string4))  # %x is a placeholder for hexadecimals
print("string4 is %f characters long!" % len(string4))  # %f is a placeholder for floats