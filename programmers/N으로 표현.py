def solution(N, number):
    """ 이전 연산 결과 + 사칙연산 한 번

    idea: dyanmic programming with BF
    """
    cache = [set() for _ in range(9)]
    for i in range(1, 9):
        cnt = int(str(N) * i)
        cache[i].add(cnt)  # add N*i number

        for k in range(1, i):  # search for before cache
            for j in cache[k]:
                for l in cache[i - k]:
                    cache[i].add(j + l)
                    cache[i].add(j - l)
                    cache[i].add(j * l)
                    cache[i].add(j // l) if j and l else None

        if number in cache[i]:
            return i

    return -1


if __name__ == '__main__':
    solution(5, 31168)
