def calcul(lst):
    result = 0
    while lst:
        p1 = lst.pop()
        # 남은 리스트 개수가 한 개
        if not lst:
            result += p1
            break
        p2 = lst.pop()
        result += max(p1 + p2, p1 * p2)
    return result


n = int(input())
answer = 0
minus, plus = [], []
for _ in range(n):
    x = int(input())
    if x == 1:
        answer += 1
        continue
    if x <= 0:
        minus.append(x)
    else:
        plus.append(x)
print(answer + calcul(sorted(plus)) + calcul(sorted(minus, reverse=True)))
