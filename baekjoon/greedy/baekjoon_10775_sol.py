import sys
"""
local optimal solution 자체가 틀린 것은 아니기 때문에, Union-Find 적용
래퍼런스는 비행기 번호를 받으면서 처리하는게 아니라, 아예 한 줄씩 들어오는 입력을 리스트로 만들고 처리를 해버리네
"""
# helper function
def find(x):
    # 자기 자신이 최상위 노드인 경우
    if parent[x] == x:
        return x
    # 자식 노드 => 부모 찾을 때까지 재귀
    return find(parent[x])

def union(x,y):
    x = find(x)
    y = find(y)
    if x < y:
        parent[y] = x
    else: # x>y
        parent[x] = y # 남은 게이트 개수

# Input
# key: number of maximum gate, value: number of left gate
num_gate, num_plane = int(sys.stdin.readline()), int(sys.stdin.readline())
parent, plane_list, result = {i: i for i in range(0, num_gate+1)}, [], 0

for _ in range(num_plane):
    plane_list.append(int(sys.stdin.readline()))

for plane in plane_list:
    x = find(plane)

    if x == 0:
        break
    union(x,x-1)
    result += 1
print(result)



