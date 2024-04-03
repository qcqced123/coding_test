def solution(n, words):
    """
    problem link:
        https://school.programmers.co.kr/learn/courses/30/lessons/12981

    summary:
        1) 영어 끝말잇기
          - 이전 등장 문자 사용 불가
            - 유니크한 집합 필요
          - 두글자 이상 단어만 가능

    solution:
        1) O(n*s*w) 이하
          - 탈락 기준
            - 이미 말한 단어 사용
            - 시작 철자가 틀린 경우
    return:
        1) 가장 먼저 탈락하는 사람 번호, 몇번째 스테이지 탈락
          - 없으면 [0,0]
    """

    def is_valid(curr_idx: int):
        return words[curr_idx][0] == words[curr_idx - 1][-1] and words[curr_idx] not in vocab

    curr_stage = 1
    vocab, answer = [words[0]], []
    for i in range(1, len(words)):
        if is_valid(i):
            vocab.append(words[i])

        else:
            answer.extend([i % n + 1, curr_stage])
            break

        if i % n == n - 1:
            curr_stage += 1
    else:
        answer.extend([0, 0])

    return answer