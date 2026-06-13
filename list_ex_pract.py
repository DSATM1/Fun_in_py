#-----List Practice-------

# lst = [23,45,9,12,78,32,21]
# uniq = list(set(lst))
# sorted_list = sorted(uniq)
# if len(uniq) < 2:
#     print(len(uniq))
# print(uniq[2])

def remove_duplicate(lst):
    uniq = list(set(lst))
    sorted_list = sorted(uniq)
    return sorted_list[-2]
print(remove_duplicate([23,45,9,12,78,32,21]))
