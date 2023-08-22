import sys

"""
[풀이 시간]
1) 15:50 ~ 16:30

[요약]
1) 명단 A, 명단 B의 교집합 구하는 문제

[전략]
1) 명단 A의 애들을 전부 사전에 넣어 주자
"""
N, M = map(int, sys.stdin.readline().split())
# result_list, name_dict = [], {}
#
# # 듣도 못한 사람 명단
# for _ in range(N):
#     name_dict[sys.stdin.readline().rstrip()] = True
#
# # 보도 못한 사람 명단
# for _ in range(M):
#     tmp_name = sys.stdin.readline().rstrip()
#     try:
#         if name_dict[tmp_name]:
#             result_list.append(tmp_name)
#     except KeyError as e:
#         pass
#
# result_list.sort()
# print(len(result_list))
# for name in result_list:
#     print(name)

set_a, set_b = set(), set()
# # 듣도 못한 사람 명단
for _ in range(N):
    set_a.add(sys.stdin.readline().rstrip())

# 보도 못한 사람 명단
for _ in range(M):
    set_b.add(sys.stdin.readline().rstrip())

result_list = sorted(list(set_a & set_b))
print(len(result_list))
for name in result_list:
    print(name)
