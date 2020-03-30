class Solution:
    def numJewelsInStones(self, J: str, S: str) -> int:
        setJ = set(J)
        # return sum(s in J for s in S)
        cnt = 0
        for c in S:
            if c in setJ:
                cnt += 1
        return cnt


if __name__ == "__main__":
    J, S = "aA", "aAAbbbb"
    print(Solution().numJewelsInStones(J, S))
