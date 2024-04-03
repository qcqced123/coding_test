def solution(nums):
    """
    problem link:
        https://school.programmers.co.kr/learn/courses/30/lessons/1845

    summary:
        1) N/2 마리 가져가기
          - 포켓몬 종류에 따라서 번호가 붙는다
            - 해시스러운 문젠데
          - 선택하되, 최대한 많은 종류로 선택
    args:
        배열값: 포켓몬 종류

    solution:
         1) O(N**2)
           - 세트를 쓰면 되지 않을까??
             - len(set(nums)) => 현재 리스트에 담긴 유니크한 종류 개수
             - len(set(nums))와 N / 2를 비교하면 될 듯
    """
    targets = len(nums) / 2
    unique = len(set(nums))
    answer = unique if targets >= unique else targets
    return answer

