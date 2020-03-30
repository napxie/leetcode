class Solution:
    def climbStairs(self, n: int) -> int:
        if n < 3:
            return n
        list = [0] * (n+1)
        list[1] = 1
        list[2] = 2
        for i in range(3, n+1):
            list[i] = list[i-1] + list[i-2]
        return list[n]

    def climbStairs1(self, n: int) -> int:
        x = y = 1
        for i in range(n):
            x, y = x + y, x
        return y


if __name__ == "__main__":
    n = 5
    print(Solution().climbStairs(n))
    print(Solution().climbStairs1(n))
