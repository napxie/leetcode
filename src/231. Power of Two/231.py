class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        return n > 0 and n & (n-1) == 0

    def isPowerOfTwo1(self, n: int) -> bool:
        if n == 0:
            return False
        while n % 2 == 0:
            n /= 2
        return n == 1


if __name__ == "__main__":
    n = 16
    print(Solution().isPowerOfTwo(n))
    print(Solution().isPowerOfTwo1(n))
