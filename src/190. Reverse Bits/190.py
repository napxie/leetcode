class Solution:
    def reverseBits(self, n: int) -> int:
        res = 0
        count = 32
        while count:
            res <<= 1
            res += n & 1
            n >>= 1
            count -= 1
        return int(bin(res), 2)


if __name__ == "__main__":
    n = 43261596
    print(Solution().reverseBits(n))
