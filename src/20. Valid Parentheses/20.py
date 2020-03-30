class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        mapping = {')': '(', ']': '[', '}': '{'}
        for c in s:
            if c not in mapping:
                stack.append(c)
            elif not stack or mapping[c] != stack.pop():
                return False
        return not stack


if __name__ == "__main__":
    s = "()[]{}"
    print(Solution().isValid(s))
