from typing import List

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        sums = 0
        for i in digits:
            sums = sums*10 + i 
        sums_str = str(sums + 1)
        return [int(j) for j in sums_str]

if __name__ == "__main__":
    digits = [1,2,3]
    print(Solution().plusOne(digits))