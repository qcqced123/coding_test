import sys
from typing import List
from collections import Counter


def solution():
    N = int(sys.stdin.readline())
    candies = list(map(int, sys.stdin.readline().split()))
    vocab = Counter(candies)


if __name__ == "__main__":
    solution()
