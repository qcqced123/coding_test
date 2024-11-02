from math import sqrt


def solution(brown, yellow):
    def is_valid(x: int) -> bool:
        y = -x + brown / 2 + 2
        return (x - 2) * (y - 2) == yellow

    answer = 0
    multiply = brown + yellow

    # get starting point
    row = int(sqrt(multiply))
    while not is_valid(row):
        row += 1

    answer = [row, multiply // row] if row > multiply // row else [multiply // row, row]
    return answer


if __name__ == '__main__':
    solution(24, 24)
