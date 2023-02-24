import sys
"""
[Reference Solution]
스케줄러 상 남은 개수의 비교는 정확한 개수를 따질 필요가 없었고, 단순하게 사용이 다시 될 것인지 정도면 충분했다.
그것보다는 현재 멀티 탭에 꽂힌 제품들이 얼마나 뒤에 다시 사용이 되는지 비교를 해줘야 모든 반례를 만족시킬 수 있었다.
"""
# Input
N, K = map(int, sys.stdin.readline().split())
item_list, multi_tab, result = list(map(int, sys.stdin.readline().split())), [0] * N, 0

for i in range(K):
    # Step 1. Multi-Tab Init & 사용 하려는 제품이 이미 꽂혀 있는 경우
    isTrue = False
    for j in range(N):
        if multi_tab[j] == 0 or item_list[i] == multi_tab[j]:
            isTrue = True
            multi_tab[j] = item_list[i]
            break
    # 멀티 탭에 제품을 꽂았거나 이미 꽂힌 제품을 그대로 사용하는 경우
    if isTrue:
        continue
    # Step 2. 이후 시점 스케줄링 유무 & 개수
    a = 0
    for j in range(N):
        # 이후 시점 스케줄링 되어 있는 경우: try~except 구문으로 처리해줘야 함
        try:
            if a < item_list[i+1:].index(multi_tab[j]):
                a = item_list[i+1:].index(multi_tab[j])
                b = j # 인덱스 저장: 몇 번째 콘센트
        # 이후 시점에 스케줄링 없는 경우
        except:
            a = -1
            b = j
            break
    multi_tab[b] = item_list[i]
    result += 1
print(result)

