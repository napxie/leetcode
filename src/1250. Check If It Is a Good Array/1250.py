from functools import reduce
from math import gcd
from typing import List

class Solution:
    def isGoodArray(self, nums: List[int]) -> bool:
        return reduce(gcd, nums) == 1