import sys


def solution():
    sys.setrecursionlimit(10**6)

    def factorial(n: int):
        if n == 1:
            return n

        answer = n*factorial(n-1)
        return answer

    print(factorial(10))

if __name__ == '__main__':
    solution()