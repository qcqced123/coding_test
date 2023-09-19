import sys
"""
[요약]
1) n x x 크기 테이블
    - 입력과 실제 인덱스 값 차이 있음
    - 주어진 구간의 모든 원소 합 구하는 프로그램 작성
    - 시간, 메모리, 입력 길이: 1초, 256, 1024
    => Tabulation 가능
[전략]
1) dp[end] = end까지 누적합 - (src-1)까지 누적합
    - 누적합 배열 만들기
    -
"""
N, M = map(int, sys.stdin.readline().split())
