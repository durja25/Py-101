from first_day import is_palindrome

def is_number_balanced(n):
    n = [int(x) for x in str(n)]
    mid = len(n)//2

    left = n[0:mid]
    right = n[mid+1:]
    right = sum(right)
    left = sum(left)

    if right == left:
        return True
    else:
        return False

def is_increasing(seq):
    if len(seq) == 1:
        return True
    first = 0
    second = 0
    for i in range(len(seq)-1):
        if seq[i] < seq[i + 1]:
            pass
        else:
            return False

    return True


def is_decreasing(seq):
    if len(seq) == 1:
        return True
    first = 0
    second = 0
    for i in range(len(seq)-1):
        if seq[i] > seq[i + 1]:
            pass
        else:
            return False

    return True

def get_largest_palindrome(n):
    for i in range(n-1,0,-1):
        if is_palindrome(i):
            return i
            break
    # pass

def prime_numbers(n):
    num = [num for num in range(2,n+1)]

    for i in range(2,n+1):
        not_p = [x for x in range(i*2,n+1,i)]
        # not_p =[]
        # for v in range(i*2,n+1,i):
        #     not_p.append(v)

        num = set(num) - set(not_p)

    return (list(num))

def is_anagram(a, b):
    print(sorted(a.lower()))
    print(sorted(b.lower()))
    if sorted(a.lower()) == sorted(b.lower()):
        return True
    else: return False

def sum_matrix(matr):
    # Using list comprehensions
    return sum([sum(row) for row in matr])

def max_char(string):
  s = string
  m =0
  res = ""
  for i in range(len(s)):
    c = 0
    for j in range(len(s)):
      if s[i] == s[j]:
        c+=1
    if (c > m):
      m = c
      res = s[i]
  return (res)

# print(max_char(s))