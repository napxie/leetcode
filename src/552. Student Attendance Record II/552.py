class Solution:
    def checkRecord(self, n: int) -> int:
        a, b, c, d, e, f = 0, 1, 1, 0, 0, 1
        for k in range(n):
            a, b, c = b, c, (a + b + c) % 1000000007
            d, e, f = e, f, (d + e + f + c) % 1000000007
        return f
