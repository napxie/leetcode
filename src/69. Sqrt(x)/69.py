class Solution:
    def mySqrt(self, x: int) -> int:
        if x <= 0:
            return x
        l, r = 1, x // 2
        while l < r:
            m = (l+r+1) >> 1
            if m * m > x:
                r = m - 1
            else:
                l = m
        return l


if __name__ == "__main__":
    x = 4
    print(Solution().mySqrt(x))
