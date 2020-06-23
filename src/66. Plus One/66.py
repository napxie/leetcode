from typing import List


class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        sums = 0
        for i in digits:
            sums = sums*10 + i
        sums_str = str(sums + 1)
        return [int(j) for j in sums_str]

    def plusOne1(self, digits: List[int]) -> List[int]:
        for i in range(len(digits)-1, -1, -1):
            digits[i] += 1
            digits[i] %= 10
            if digits[i] != 0:
                return digits
            # if digits[i] != 9:
            #     digits[i] += 1
            #     return digits
            # digits[i] = 0
        digits = [0] * (len(digits) + 1)
        digits[0] = 1
        return digits
if __name__ == "__main__":
    digits = [1, 2, 3]
    print(Solution().plusOne(digits))
