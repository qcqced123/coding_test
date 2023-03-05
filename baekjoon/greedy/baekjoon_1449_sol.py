import sys
"""
[Idea]
- 오름 차순 정렬을 사용해 구멍 위치 정보 배열을 정렬
- 이후 배열의 시작점에 테이프를 붙인다고 가정
- 이후 루프를 활용해 배열로 부터 구멍의 위치값을 전달 받으며 테이프의 오른쪽 끝 인덱스값과 비교를 진행
- 이때, 구멍의 인덱스 값이 테이프의 오른쪽 끝 인덱스 값보다 큰 경우, 사용한 테이프 개수를 1개씩 증가
- 위 과정을 배열의 마지막 원소까지 지속적으로 반복한다.
"""
N, L = map(int, sys.stdin.readline().split())
hole_idx, result = list(map(int, sys.stdin.readline().split())), 0
hole_idx.sort()
tape_idx = 0
for i in hole_idx:
    if tape_idx < i:
        result += 1
        tape_idx = i + L - 1
print(result)
