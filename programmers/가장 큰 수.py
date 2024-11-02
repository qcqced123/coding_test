def solution(numbers):
    answer = []

    arr = list(map(str, numbers))
    arr.sort()

    i = 0
    while i < len(arr):
        cache = []
        if i == len(arr) - 1 or arr[i][0] != arr[i + 1][0]:
            answer.append(arr[i])
            i += 1

        else:
            p = i
            while True:
                temp = arr[p]
                addit = temp[:4 - len(temp)] if len(temp) > 1 else temp * 3
                cache.append((temp + addit, len(temp)))

                if p == len(arr) - 1 or arr[p][0] != arr[p + 1][0]:
                    break

                p += 1

            cache.sort()
            for c in cache:
                seq, length = c
                answer.append(seq[:length])

            i = p + 1

    result = "".join(answer[::-1])
    return "0" if result[0] == "0" else result


if __name__ == '__main__':
    solution([3, 34, 30, 5, 9])
