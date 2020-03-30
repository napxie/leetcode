from typing import List


class Solution:
    def countBits(self, num: int) -> List[int]:
        def countnum(x):
            count = 0
            while x != 0:
                x = x & (x - 1)
                count += 1
            return count
        bits = [0]
        for i in range(1, num+1):
            bits.append(countnum(i))
        return bits


if __name__ == "__main__":
    num = 5
    print(Solution().countBits(num))
