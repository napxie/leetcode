class Solution:
    def reverseBits(self, n: int) -> int:
        res, count = 0, 32
        while count:
            res <<= 1
            res += n & 1
            n >>= 1
            count -= 1
        return int(bin(res), 2)

    def reverseBits1(self, n: int) -> int:
        res, count = 0, 31
        while n:
            res += (n & 1) << count
            n = n >> 1
            count -= 1
        return res

if __name__ == "__main__":
    n = 43261596
    print(Solution().reverseBits(n))
    print(Solution().reverseBits1(n))
