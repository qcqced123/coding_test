
def solution(n, k):
    """ 줄 세우기, 사전순 나열에서 K번쨰 배열 리턴
    idea: implementation
        - 20!이라서 backtracking 불가능

    feedback:
        - 모듈러 연산으로 순열을 구현하는게 맞음
        - 아니 다음 자리도 똑같이 하는게 맞다는데 왜 틀린거지,,,,,,,,
        - 다 맞는데,,,, 뭐지 진짜 구현을 그지... 같이.... 한건
        - 굳이 어렵게 배열 조작 하지말고, 어차피 길이가 크지도 않은데 pop()을 써서 확실하게 빼버려라....

    """
    answer = []
    visited = [0 ] *n

    for i in range( n -1, 0, -1):
        cache = i
        for j in range( i -1, 0, -1):
            cache *= j

        pos = k // cache
        k %= cache
        if k: pos += 1
        l, cnt = 0, 0
        while l < n and cnt < pos:
            if not visited[l]:
                cnt += 1

            if cnt == pos:
                visited[l] = 1
                answer.append( l +1)
                break

            l += 1

    for j in range(n):
        if not visited[j]:
            answer.append( j +1)

    return answer


def solution2(n, k) -> list:
    from math import factorial
    k -= 1
    answer = []
    numbers = list(range(1, n+1))

    while numbers:
        idx, k = divmod(k, factorial(len(numbers)-1))  # divmod: 몫과 나머지를 리턴함
        answer.append(numbers.pop(idx))

    return answer


if __name__ == '__main__':
    print(solution2(4, 11))
