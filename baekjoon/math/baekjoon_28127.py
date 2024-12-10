import sys


def solution():
    """ QlogA
    idea: math
        - 등차수열의 합
    """
    def calculate(x, a, d):
        return x**2 + (2*a-d)*x

    input = sys.stdin.readline
    queries = [list(map(int, input().split())) for _ in range(int(input()))]
    for query in queries:
        a, d, x = query
        # get position of y-axis
        i, total = 1, 1
        while True:
            cnt = a + (i-1)*d
            if total + cnt > x:
                break
            i += 1
            total += cnt

        print(i, x-total+1)


if __name__ == "__main__":
    solution()
