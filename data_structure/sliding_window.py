import sys


def longest_palindrome(s: str) -> str:
    """ method for finding longest palindrome in string handle problem """
    def expand(left: int, right: int) -> str:
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        return s[left + 1:right]  # method가 return 하는 상황은 left와 right이 가리키는 철자는 펠린드롬이 아니라는 의미니까 빼줘야 한다.

    # 예외 처리: 한 글자 혹은 전체가 펠린드롬
    if len(s) < 2 or s == s[::-1]:
        return s

    result = ''
    for i in range(len(s) - 1):  # for out of index
        result = max(
            result,
            expand(i, i + 1),
            expand(i, i + 2),
            key=len
        )
    return result


if __name__ == '__main__':
    word = 'babba'
    longest_palindrome(word)

