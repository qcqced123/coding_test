from collections import Counter
import sys
"""
[풀이 시간]
1) 08:50 ~ 09:20

[규칙]
1) 멀티 탭 구멍 & 전기 용품 사용 순서가 있을 때, 플러그 빼는 횟수를 '최소화' 해보자
2) N => 멀티탭 구멍 개수
3) K => 스케줄 길이

[전략]
- 어차피 멀티탭 구멍 개수 상한이 100개, 스케줄 길이 상한 역시 100개라서 시간적 압박은 없을 듯
- 관건은 멀티 탭에 플러그가 꽉 차 있는 상태에서, 다음 스케줄을 실행할 때 어떤 플러그를 뺄 것인가 그게 중요함
  일단 어떤 전략을 사용하건, 플러그를 꽉차게 만들어야 하기 때문에 그 전까지는 구현을 해보자
  우선 순위 큐! => 힙으로 구현
- [남은 개수, 전자 제품 이름]
- Step 1. 콘센트 꽉 채우기
- Step 2. 현재 콘센트에 있는 전자 제품의 스케줄 상 남은 횟수 비교, 적은거 빼기
- 반례 보니까 진짜 그렇네.... 내 방식으로 풀면 틀리네...... 오히려 많아지는 경우도 생겨버림
- 스케줄 상 남은 개수 기준이 아니라
"""
N, K = map(int, sys.stdin.readline().split())
# 전자 제품 이름, 멀티 탭에 꽂힌 아이들 중에서 남은 스케줄 개수, 멀티 탭에 꽂힌 전자 제품 이름, 결과
item_list, plug_list, temp_list, result = list(map(int, sys.stdin.readline().split())), [999] * (K+1), [], 0
counter = dict(Counter(item_list))
for idx in range(len(item_list)):
    if item_list[idx] in temp_list:
        counter[item_list[idx]] -= 1
        plug_list[item_list[idx]] = counter[item_list[idx]]
        continue
    # 멀티탭에 남은 칸이 있는 경우
    if len(temp_list) < N:
        counter[item_list[idx]] -= 1
        temp_list.append(item_list[idx])
        plug_list[item_list[idx]] = counter[item_list[idx]]
        continue

    # 이 때 필요한 게 다시 사용되는지 여부랑 얼마나 뒤에 사용되는지 => 여기 구현 다시하기
    counter[item_list[idx]] -= 1
    out_item = plug_list.index(min(plug_list)) # 빼낼 아이템 선택
    print(out_item)
    plug_list[out_item] = 999 # 빼낸 아이템은 다시 999로 초기화
    temp_list[temp_list.index(out_item)] = item_list[idx] # 멀티 탭에 현재 대상 아이템 꽂자
    plug_list[item_list[idx]] = counter[item_list[idx]]
    result += 1

print(result)


