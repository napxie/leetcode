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

    def mySqrt1(self, x: int) -> int:
        if x == 0:
            return 0
        cur = 1
        while True:
            pre = cur
            cur = (cur + x / cur) / 2
            if abs(cur - pre) < 1e-6:
                return int(cur)

                
if __name__ == "__main__":
    x = 4
    print(Solution().mySqrt(x))
