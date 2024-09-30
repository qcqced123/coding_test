import sys


def solution():
    """ 문제 개길어 미친, 그냥 구하면 되는거 아니야?
    idea:
        1) 주어진 s/n를 기약 분수 형태로 만들기
            - 최대 공약수 구해서 나누기
        2) 모듈러 곱셈의 역원 구하기
    """
    def get_gcd(a: int, b: int):
        while b:
            a, b = b, a % b
        return a

    M = int(input())
    result = 0
    modular = 1000000007
    for _ in range(M):
        # get greatest common divisor
        vn, vs = map(int, sys.stdin.readline().split())
        gcd = get_gcd(vs, vn) if vs > vn else get_gcd(vn, vs)

        # get 기약 분수
        n, s = vn/gcd, vs/gcd

        # value of reverse modular mul


if __name__ == "__main__":
    solution()
