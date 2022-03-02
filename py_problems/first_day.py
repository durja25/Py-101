# 1. Sum of all digits of a number

def sum_of_digits(n):
    n = abs(n) # clearing if negative no is passed
    sum = 0
    for i in str(n): # converting int to str to iterate given no & adding it to sum
        sum += int(i)
    return (sum)

    # pass



def to_digits(n):
    # converting given no to list of digits
    n = abs(n)
    return list(map(int, str(n)))

# def to_digits(n):
#     n = abs(n)
#     return [int(x) for x in str(n)]

print(to_digits(-123))

def to_number(n):
    # coverting list to number
    new = []
    for i in n:
        if int(i) == i:
            # checking if its int and converting it to str
            new.append(str(i))
        else:
            # if its already str then just add it to list
            new.append(i)
    return(' '.join(new))


# print(to_number(['0', '1']))


def factorial_digits(n):
    # The factorial of a number is the function that multiplies the number by every natural number below it
    # e.g. - 1 * 2 * 3 * 4 * 5 = 120
    fact = 1
    for i in range(1,n+1):
        fact = fact * i
    return fact


def fibonacci_digit(n):
    # The Fibonacci numbers are the numbers in the following integer sequence.
    # 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144
    if n<=1:
        return n

    else:
        return fibonacci_digit(n - 1) + fibonacci_digit(n -2)

print(fibonacci_digit(10))


def fibonacci_series(n):
    # The Fibonacci numbers are the numbers in the following integer sequence.
    # 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144
    # prints all series
    l = [0,1]
    for i in range(n+1):
        next_num = l[-1] + l[-2] #Add last two numbers in sequence.
        l.append(next_num)
    return l

# print(to_number(fibonacci_series(10)))


def is_palindrome(n):
    n = str(n)
    if (n == n[::-1]):
        return True
    else:
        return False

# print(is_palindrome("121"))


def count_vowels(string):
    n =0
    for char in string.lower():
        if char in "aeiouy":
            n+=1
    return n



def count_consonants(string):
    n =0
    for char in string.lower():
        if char in "bcdfghjklmnpqrstvwxz":
            n+=1
    return n

# print(count_consonants("python"))

def char_histogram(string):
    d = {}
    for i in string:
        keynum = string.count(i)
        d[i] = keynum
    return (d)

print(char_histogram("AAAAaaa!!!"))