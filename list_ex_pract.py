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

"""for i in range(1,11):
    print(f"Table of {i}")
    for j in range(1, 11):
        print(f"{i} X {j} = {i*j}")"""

"""for i in range(1,51):
    if i%3==0 or i%7==0:
        continue
    print(i,end=" ")"""


"""n = int(input("Enter n: ").strip())
if n <= 0:
    print("Please Enter a Positive Number")
else:
    step = 0
    while n != 1:
        print(n, end = " -> ")
        if  n % 2 == 0:
            n = n//2
        else:
            n = n*3+1
        step += 1
    print(n)
    print(f"Steps : {step}")"""

