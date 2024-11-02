def solution(strings, n):
    strings.sort(key=lambda x: (x[n], x))
    return strings


if __name__ == '__main__':
    solution(["abce", "abcd", "cdx"], 2)
