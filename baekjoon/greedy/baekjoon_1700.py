import sys, heapq
from collections import Counter
"""
[풀이 시간]
1) 14:40 ~ 15:30

[규칙]
1) 멀티 탭 구멍 & 전기 용품 사용 순서가 있을 때, 플러그 빼는 횟수를 '최소화' 해보자
2) N => 멀티탭 구멍 개수
3) K => 스케줄 길이

[전략]
- 어차피 멀티탭 구멍 개수 상한이 100개, 스케줄 길이 상한 역시 100개라서 시간적 압박은 없을 듯
- 관건은 멀티 탭에 플러그가 꽉 차 있는 상태에서, 다음 스케줄을 실행할 때 어떤 플러그를 뺄 것인가 그게 중요함
  일단 어떤 전략을 사용하던, 플러그를 꽉차게 만들어야 하기 때문에 그 전까지는 구현을 해보자
  우선 순위 큐! => 힙으로 구현
- [남은 개수, 전자 제품 이름]
- Step 1. 콘센트 꽉 채우기
- Step 2. 현재 콘센트에 있는 전자 제품의 스케줄 상 남은 횟수 비교, 적은거 빼기
=> 이게 남은 개수랑 전자 기기 이름이랑 매칭 시키는 게 힘들구나
"""
# Input
N, K = map(int, sys.stdin.readline().split())
multi_tab, multi_tab_list, schedule, result = [], [], list(map(int, sys.stdin.readline().split())), 0
counter = dict(Counter(schedule))

for i in range(K):
    # Step 1. 콘센트 꽉 채우기
    if len(multi_tab) != N:
        counter[schedule[i]] -= 1 # 큐에 넣기 전에 개수 하나 빼줘야지
        multi_tab_list.append(schedule[i])
        heapq.heappush(multi_tab, [counter[schedule[i]], schedule[i]]) # [개수, 전자 제품]
        continue
    # Step 2. 스케줄 대상 전자 기기가 이미 꽂혀 있는 경우
    if schedule[i] in multi_tab_list:
        counter[multi_tab[i][0]] -= 1
        continue
    # Step 3. 멀티 탭에서 콘센트 빼야 하는 경우
    result += 1
    idx = multi_tab_list.index(schedule[i])
    multi_tab_list[idx] = schedule[i]
    heapq.heappop(multi_tab)
    heapq.heappush(multi_tab, [counter[schedule[i]], schedule[i]]) # [개수, 전자 제품]

print(result)

