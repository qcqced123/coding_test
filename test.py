# test = [1,2,3,4,5]
# hp = test[0]
# hp -= 1
#
# print(hp)
# print(test)
#
#
# # arr = []
# # print(arr[1])
#
#
# test = set()
# test.add(1)
# print(test)
# test.remove(1)
# print(test)
#
#
# test = [(2,14,1), (3,8,1), (5,12,1)]
# test.sort(key=lamb)

group_a = {1,2,3,4}
group_b = {4,5,6,7}

print(group_b - group_b.intersection(group_a))
print(group_b.difference(group_a))