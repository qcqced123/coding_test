import sys, heapq

"""
[풀이 시간]
1) 15:00 ~ 15:30

[규칙]
1) 각 단어는 알파벳 대문자로만 구성, 대문자를 0~9 숫자 중 하나에 대응시켜 N개의 수를 합하는 문제
2) 같은 알파벳은 항상 같은 숫자로 변환, 두 개 이상이 같은 숫자로 바뀌면 안된다
3) 알파벳에 대응시키는 숫자는 예시마다 달라지네 => 그저 단어의 합이 최대가 되도록 맵핑하면 되는구나

[변수]
N => 수학 문제를 구성하는 단어 개수

[아이디어]
1) 숫자가 최대값을 가질라면, 자리수가 중요함, 자리수가 동일할 때는 가장 높은 숫자를 배정하는 것이 유리함
2) max_heap 사용해서 입력 받으면서 자리수 대로 정렬 해버려야함 
=> 알파벳:인덱스 형태로 저장
=> 인덱스 높은 순서대로 숫자 적용
=> 문자열 루프로 하나씩 받으면서 딕셔너리 접근, 대응된 숫자로 바꿔주기

[반례]
10개의 문자열이 아래와 같이 입력되는 경우:
ABB
BB
BB
BB
BB
BB
BB
BB
BB
=> A = 10*10, B = 11*10
=> B에 총 곱하는 "자리수" 값이 더 크기 때문에 B에 9를 할당하고 A에 8을 할당하는 것이 최대값을 도출할 수 있음
=> 위와 같은 상황을 해결할 수 없기 때문에 자리수 개념으로 접근해야 함!
"""

# Input
num_list = [i for i in range(9, -1, -1)]
word_list, result, vocab, temp_vocab = [], [], {}, {}

# Max HeapSort
for i in range(int(sys.stdin.readline())):
    idx = -1
    word = input()
    heapq.heappush(word_list, (-len(word), word))
    for value in word:
        idx += 1
        try:
            if len(word) - idx > vocab[value]:
                vocab[value] = len(word) - idx
        except:
            vocab[value] = len(word) - idx

# 딕셔너리 값 기준 내림차순 정렬, 실제 숫자로 바꾸기
vocab = sorted(vocab.items(), key=lambda x:x[1], reverse=True)
for idx, value in enumerate(vocab):
    value = list(value)
    temp_vocab[value[0]] = num_list[idx]

# 문자열 루프로 하나씩 받으면서 딕셔너리 접근, 대응된 숫자로 바꿔주기
for i in range(len(word_list)):
    temp_word = ''
    for value in word_list[i][1]:
        temp_word += str(temp_vocab[value])
    result.append(int(temp_word))

print(sum(result))

