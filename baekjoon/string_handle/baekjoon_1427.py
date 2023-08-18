import sys
from collections import Counter

"""
[시간]
1) 23:50 ~ 24:03

[요약]
1) 수의 각 자리수를 내림차순
 - 2143: 4321
[전략]
1) 입력 받는 숫자를 split으로 잘라서 다시 sort 해야지
    - split, Counter, sort 같이 사용하면 될 듯
"""
n = list(sys.stdin.readline().rstrip())
count = Counter(n)
tmp_result = sorted(count.elements(), reverse=True)
print(int(''.join(tmp_result)))

