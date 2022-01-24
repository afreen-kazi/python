# list1 = [6, 3, 2, 6, 5]
# print(list1)
# maximum = max(list1)
# list1.remove(maximum)
# for i in range(0, len(list1)-1):
#     if list1[i] == maximum:
#         list1.remove(maximum)
#
# print(max(list1))

list = [6, 3, 2, 6, 5]
set1 = set(list) # set will remove duplicate elements
print(set1)
# print(sorted(set(set1))[-2]) # -2 will print second last element after sorting
print(sorted(set1)[-2])