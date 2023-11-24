import sys
from typing import List
"""
[풀이]
1) 모든 약수의 합: f(A)
    - g(x): x보다 작거나 같은 모든 자연수 y의 f(y)값
    => 입력값 이하 모든 자연수의 f(A)
    => 딱히 약수의 합에 대한 규칙이 안보임
    => 그냥 나누고 계속 더해주는 수밖에 없을 듯..?
    => 이것도 몰겠는데...?
"""


def solution():
    for _ in range(int(sys.stdin.readline())):
        N = int(sys.stdin.readline())


if __name__ == "__main__":
    solution()
