def solution(arr1, arr2):
    """
    Problem link:
        https://school.programmers.co.kr/learn/courses/30/lessons/12949

    O(N**3) 풀이
      - 1) 왼쪽 행렬의 행벡터 접근
      - 2) 오른쪽 행렬의 열벡터 접근
    """
    answer = []
    for y in range(len(arr1)):
        curr = []
        for z in range(len(arr2[0])):
            cnt = 0
            for x in range(len(arr1[0])):
                cnt += arr1[y][x] * arr2[x][z]
            curr.append(cnt)
        answer.append(curr)
    return answer