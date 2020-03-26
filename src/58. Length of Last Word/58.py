class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        lens = len(s)
        if s and s[lens-1] == ' ':
            n = lens - 1
            while n >= 0 and s[n] == ' ':
                n -= 1
            s = s[:n+1]
        # s = s.strip()
        if s == '': return 0
        for i in range(len(s)-1, -1, -1):
            if s[i] == ' ':
                return (len(s)-i-1)
        return len(s)

if __name__ == "__main__":
    s = "Hello World"
    print(Solution().lengthOfLastWord(s))