from typing import Tuple, List


def solution(arr: List, n: int, mode: str = "clockwise") -> List:
    """
    problem link:

    implementation:
    """
    row, col = len(arr), len(arr[0])
    result = [[0] * col for _ in range(row)]

    def clockwise_rotate() -> None:
        for i in range(row):
            for j in range(col):
                result[i][j] = arr[row-1-j][i]

    def counter_clockwise_rotate() -> None:
        for i in range(row):
            for j in range(col):
                result[i][j] = arr[j][col-1-i]

    rotate_fn = clockwise_rotate if mode == "clockwise" else counter_clockwise_rotate
    for _ in range(n):
        rotate_fn()

    return result


if __name__ == '__main__':
    original = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16],]
    grid = solution([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16],], 1, mode="counter_colockwise")

    for i in range(len(grid)):
        print(original[i], end='\n')

    print()

    for i in range(len(grid)):
        print(grid[i], end='\n')