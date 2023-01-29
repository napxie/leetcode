class Solution:
    def getLucky(self, s: str, k: int) -> int:
        digits = "".join(str(ord(ch)-ord("a")+1) for ch in s)
        for i in range(k):
            if len(digits) == 1:
                break
            total=sum(int(ch) for ch in digits)
            digits = str(total)
        return int(digits)

if __name__ == "__main__":
    s = "leetcode"
    k = 2
    print(Solution().getLucky(s, k))