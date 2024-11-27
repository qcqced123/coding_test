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

N, S = map(int, input().split())

answer = 0  # 최대합
array = [[0, 0]]
dp = [0] * (N + 1)  # i ~ N 번째 중 최대합 금액 저장
height = [0] * (N + 1)  # i번째 그림을 전시한다고 할 때, 앞에 전시할 수 있는 가장 높은 그림

for i in range(N):
    H, C = map(int, input().split())
    array.append([H, C])
array.sort()  # height 순으로 정렬한다.

for i in range(1, N + 1):
    height[i] = height[i - 1] + 1
    while height[i] < i:  # i번 앞에 있는 것들 확인
        if array[i][0] - array[height[i]][0] < S:  # 조건을 만족하지 못하는 경우
            break
        height[i] += 1  # S 간격을 만족하면 index 를 하나 더 늘린다.
    height[i] -= 1  # i 번째가 조건을 만족하지 못했으므로 -1 한다.

print(height)

for i in range(1, N + 1):
    dp[i] = max(dp[i - 1], dp[height[i]] + array[i][1])

print(dp[N])
