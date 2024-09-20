def longest_palindrome(inputs: str) -> str:
    """ sliding window with two pointer algorithm
    1) init two window pointer
        - size: odd, even => 3, 2
    2) start at most left of string
    3) iter:
        - check if current state is palindrome or will be expanded state is palindrome
            - True: expand and check again current state, until not palindrome
            - False: save current state's length, init size of two window pointer, slide window

        - handling exception:
            1) given word is already palindrome
            2) given word's length is 1
    """
    def expand(left: int, right: int) -> str:
        while left >= 0 and right < len(inputs) and inputs[left] == inputs[right]:
            left -= 1
            right += 1
        return inputs[left + 1:right]

    # if input string is already palindrome or cannot be palindrome
    if len(inputs) < 2 or inputs == inputs[::-1]:
        return inputs

    result = ''
    for i in range(len(inputs) - 1):
        result = max(
            result,
            expand(i, i + 1),
            expand(i, i + 2),
            key=len
        )
        print(f"num of iter: {i}")
        print(f"current longest state: {result}")
    return result


if __name__ == '__main__':
    word = "baaaabasseesae"
    print(longest_palindrome(word))



