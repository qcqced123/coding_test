from typing import List


class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        def dfs(index: int, path: str) -> None:
            if len(path) == len(digits):
                result.append(path)
                return

            for i in range(index, len(digits)):
                for j in num2str[int(digits[i])]:
                    dfs(i + 1, path + j)

        if not digits:
            return []

        num2str = {2: 'abc', 3: 'def', 4: 'ghi', 5: 'jkl', 6: 'mno', 7: 'pqrs', 8: 'tuv', 9: 'wxyz'}

        result, word = [], ''
        dfs(0, word)
        return result

