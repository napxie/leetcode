class Solution:
    def toLowerCase(self, str: str) -> str:
        s = ''
        for c in str:
            if ord(c) >= 65 and ord(c) <= 90:
                c = chr(ord(c)+32)
            s = s + c
        return s


if __name__ == "__main__":
    str = "Hello"
    print(Solution().toLowerCase(str))
