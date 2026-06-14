#-----List Practice-------

# lst = [23,45,9,12,78,32,21]
# uniq = list(set(lst))
# sorted_list = sorted(uniq)
# if len(uniq) < 2:
#     print(len(uniq))
# print(uniq[2])

"""def second_largest(lst):
    uniq = list(set(lst))
    sorted_list = sorted(uniq)
    if len(uniq) <2:
        return None
    return sorted_list[-2]
res = second_largest([5,5,5])
print(res)"""


"""def remove_duplicate(lst):
    uniq = list(set(lst))
    sorted_list = sorted(uniq)
    return sorted_list[-2]
print(remove_duplicate([23,45,9,12,78,32,21]))"""


"""n = 5
for i in range(0,n):
    for j in range(0, i+1):
        print("*",end= " ")
    print()"""

"""n = 5
for i in range(1,n+1):
    for j in range(i,n+1):
        print("*",end= " ")
    print()"""


"""n = 5
for i in range(1,n+1):
    for j in range(1, i+1):
        print(i,end= " ")
    print()"""

n = 5  # Size of diamond

# TOP PART - Getting wider
for i in range(n):
    spaces = n - i - 1      # How many spaces before stars
    stars = 2 * i + 1       # How many stars to print
    print(" " * spaces + "*" * stars)

# BOTTOM PART - Getting narrower
for i in range(n-2, -1, -1):
    spaces = n - i - 1      # How many spaces before stars
    stars = 2 * i + 1       # How many stars to print
    print(" " * spaces + "*" * stars)