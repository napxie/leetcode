class Solution:
    def minimumMoves(self, s: str) -> int:
        covered = -1
        res = 0
        for i, c in enumerate(s):
            if c == 'X' and i > covered:
                res += 1
                covered = i + 2
        return res
    # 贪心算法
     def minimumMoves1(self, s: str) -> int:
        ans = i = 0
        while i < len(s):
            if s[i] == "X":
                ans += 1
                i += 3
            else:
                i += 1
        return ans


    
    if __name__ == "__main__":
        s = "XXOX"
        print(Solution().minimumMoves(s))
                