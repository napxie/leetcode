class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n < 0:
            x = 1 / x
            n = -n
        pow = 1
        while n:
            if n & 1:
                pow *= x
            x *= x
            n >>= 1
        return pow


if __name__ == "__main__":
    x, n = 2.00000, 10
    print(Solution().myPow(x, n))
