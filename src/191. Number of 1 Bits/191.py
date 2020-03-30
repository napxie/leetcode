class Solution:
    def hammingWeight(self, n: int) -> int:
        count = 0
        while n:
            n = n & (n-1)
            count += 1
        return count


if __name__ == "__main__":
    n = 127
    print(Solution().hammingWeight(n))
