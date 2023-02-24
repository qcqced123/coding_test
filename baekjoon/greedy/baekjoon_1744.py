import sys

'''
[풀이 시간]
1) 19:30 ~ 20:00 

[규칙]
1) 길이 N 수열의 합을 구하기, 단순 덧셈이 아니라 "두 수"를 묶어서
2) "이웃항이 아니어도" 묶을 수 있음, 자기 자신을 묶는 것은 불가능
=> 수열을 내 맘대로 정렬해도 괜찮다
3) 묶은 항들은 서로 "곱하고" 수열의 합을 구한다, 합의 최대값을 출력!
=> 곱이 최대가 되도록 만들면 되겠다.
=> 최대 힙정렬을 사용해서 수열을 내림차순으로 정의하고 두 개씩 단순하게 묶어서 곱하고 결과를 활용해 더하려고 했는데
=> 생각 해보면 방금 그 문제랑 달라질게 없어진다. 
4) 수열의 모든 수는 단 한번만 묶거나, 아니면 묶지 않아야한다.
=> 0이 존재하는 경우는...안 곱하는게 낫다 (다만 수열에 음수가 존재하면 0이랑 곱해서 없애는게 최종합은 더 크겠다)

[변수]
N => 입력된 수열의 길이, 수열에는 음수도 존재함

[아이디어]
1) 결국 중요한 것은 음수 개수...
=> 음수 개수가 짝수개: 음수끼리 곱하자
=> 음수 개수가 홀수개: 1개 남을 때 까지 음수끼리 곱하자
   => 만약 0이 있다면 0과 곱해버릴 것
   => 만약 0이 없다면 제일 작은 수를 남겨서 더할 것
   => 이렇게 하려면 양수,음수(0포함) 따로 받는 것이 나을 듯
   => 나중에 zip 해서 한번에 정렬

2) max(p1 + p2, p1 * p2) 활용 
=> 역시 이렇게 하는게 제일 최적화 된 알고리즘일 것 같았다


[pain point]
1) heapsort는 서로 다른 부호의 숫자와 0이 섞이면 정렬이 제대로 안된다
=> 부호 별로 나눠서 서로 다른 리스트에 넣는 것이 좋아 보인다
2) 어차피 수열의 숫자가 크지 않고, 지속적으로 리스트를 업데이트 할 필요가 없기 때문에 그냥 일반 정렬을 사용하자
'''

# Input
num_list, positive_list, negative_list, negative_count, zero_count = [], [], [], 0, 0
for _ in range(int(sys.stdin.readline())):
    num = int(sys.stdin.readline())
    # 양수 리스트
    if num > 0:
        positive_list.append(num)

    if num < 0:
        negative_list.append(num)
        negative_count += 1

    if num == 0:
        negative_list.append(num)
        zero_count += 1

# 리스트 정렬
positive_list.sort(reverse=True)
negative_list.sort() # 음수는 오름차순으로 정렬

# 양수
temp_positive, temp_negative = 0, 0
for idx in range(0, len(positive_list), 2):
    # 리스트 길이가 홀수 & 마지막 항
    if len(positive_list) % 2 == 1 and idx == len(positive_list) - 1:
        temp_positive += positive_list[idx]
        break

    if len(positive_list) % 2 == 0 and idx == len(positive_list) - 1:
        break

    if positive_list[idx] == 1 or positive_list[idx+1] == 1:
        temp = positive_list[idx] + positive_list[idx+1]
        temp_positive += temp

    else:
        temp = positive_list[idx] * positive_list[idx+1]
        temp_positive += temp
# 음수
for idx in range(0, len(negative_list), 2):
    if negative_count == 0:
        break
    # 음수 개수가 짝수
    if negative_count % 2 == 0:
        if idx == negative_count - 1:
            break
        temp = negative_list[idx] * negative_list[idx+1]
        temp_negative += temp
    # 음수 개수가 홀수
    if negative_count % 2 == 1:
        # 음수 리스트에 0이 없는 경우
        if zero_count == 0:
            if idx == negative_count - 1:
                temp_negative += negative_list[idx]
                break
            temp = negative_list[idx] * negative_list[idx + 1]
            temp_negative += temp
        # 음수 리스트에 0이 있는 경우
        else:
            if idx == negative_count - 1:
                break
            temp = negative_list[idx] * negative_list[idx + 1]
            temp_negative += temp

print(temp_positive + temp_negative)
