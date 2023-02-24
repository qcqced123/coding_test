import sys
"""
- 최대 힙 정렬을 사용해 지속적으로 비행기 포트 번호 업데이트하고
  현재 시점 비행기까지 생각한 포트 숫자가 가능한 포트 숫자보다 많으면 종료
- 예외 처리: 현재 시점 게이트 번호 < 해당 게이트 번호가 나온 횟수 
"""
# Input
G, gate_list, counter, max_num, result = [0]*(int(sys.stdin.readline()) + 1), [], [], 0, 0

for _ in range(int(sys.stdin.readline())):
    num = int(sys.stdin.readline())
    # 예외 처리
    if G[num] >= num:
        break
    # 최대 가능한 게이트 개수 업데이트
    if num >= max_num:
        max_num = num

    # 현재 시점 포트 숫자가 가능한 포트 숫자보다 많으면 종료
    if result >= max_num:
        break
    G[num] += 1
    result += 1 # 도킹 가능 비행기 수 업데이트

print(result)
