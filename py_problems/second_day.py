# Is Number Balanced?

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




# print(is_number_balanced(1238033))
# print(is_number_balanced(28471))
print(is_number_balanced(2))

