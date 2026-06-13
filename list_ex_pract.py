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


"""def bubble_sort(lst):
    for i in range(len(lst) -1):
        for j in range(len(lst)- i -1):
            if lst[j] > lst[j+1]:
                lst[j],lst[j+1] = lst[j+1] , lst[j]
    return lst
print(bubble_sort([64, 34, 25, 12]))"""

"""def two_sum(lst,target):
    for i in range(len(lst)):
        for j in range(i+1 ,len(lst)):
            if lst[i] + lst[j] == target:
                return [i,j]
    return -1
print(two_sum([2, 7, 11, 15], 26))"""

"""def rotate(lst,k):
    if len(lst) == 0:
        return lst
    k = k % len(lst)

    return lst[-k:] + lst[:-k]
print(rotate([1,2,3,4,5],2))"""

"""def find_missing(lst):
    n = len(lst) + 1
    for num in range(1, n+1):
        if num not in lst:
            return num
print(find_missing([1,2,4,5]))"""