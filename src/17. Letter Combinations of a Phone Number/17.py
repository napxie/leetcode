from typing import List


class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        conversion = {'2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl',
                      '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'}
        if len(digits) == 0:
            return []
        res = ['']
        for k in digits:
            for i in res:
                for j in conversion[k]:
                    res = res + [i+j]
                res.remove(i)
            # res=[i+j for i in res for j in conversion[k]]
        return res

    def letterCombinations1(self, digits: str) -> List[str]:
        phone = {'2': ['a', 'b', 'c'],
                 '3': ['d', 'e', 'f'],
                 '4': ['g', 'h', 'i'],
                 '5': ['j', 'k', 'l'],
                 '6': ['m', 'n', 'o'],
                 '7': ['p', 'q', 'r', 's'],
                 '8': ['t', 'u', 'v'],
                 '9': ['w', 'x', 'y', 'z']}

        def backtrack(combination, next_digits):
            if len(next_digits) == 0:
                output.append(combination)
            else:
                for letter in phone[next_digits[0]]:
                    backtrack(combination+letter, next_digits[1:])
        output = []
        if digits:
            backtrack("", digits)
        return output


if __name__ == "__main__":
    digits = "23"
    print(Solution().letterCombinations(digits))
    print(Solution().letterCombinations1(digits))
