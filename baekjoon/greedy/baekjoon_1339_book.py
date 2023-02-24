import sys, heapq

# Input
num_list = [i for i in range(9, -1, -1)]
word_list, result, weight, vocab = [], [], {}, {}

# Max HeapSort
for i in range(int(sys.stdin.readline())):
    idx = -1
    word = input()
    heapq.heappush(word_list, (-len(word), word))
    for value in word:
        idx += 1
        try:
            weight[value] += 10**(len(word)-idx-1)
        except:
            weight[value] = 10**(len(word)-idx-1)

# 딕셔너리 값 기준 내림차순 정렬, 실제 숫자로 바꾸기
weight = sorted(weight.items(), key=lambda x:x[1], reverse=True)
for idx, value in enumerate(weight):
    value = list(value)
    vocab[value[0]] = num_list[idx]

# 문자열 루프로 하나씩 받으면서 딕셔너리 접근, 대응된 숫자로 바꿔주기
for i in range(len(word_list)):
    temp_word = ''
    for value in word_list[i][1]:
        temp_word += str(vocab[value])
    result.append(int(temp_word))

print(sum(result))


