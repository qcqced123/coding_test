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

from bisect import bisect_left, bisect_right

x = 9
test = [1, 7, 7, 7, 10, 10, 11, 12, 13, 14]

print(bisect_right(test, x))
print(bisect_left(test, x))
