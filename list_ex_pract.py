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

"""def flatten(lst):
    result = []
    for i in lst:
        for j in i:
            result.append(j)
    return result
print(flatten([[1,2], [3,4], [5,6]]))"""


"""def linear_search(lst,target):
    for index,value in enumerate(lst):
        if value == target:
            return index
    return -1

print(linear_search([10, 25, 3, 78, 45], 78))
print(linear_search([10, 25, 3, 78, 45], 99))"""