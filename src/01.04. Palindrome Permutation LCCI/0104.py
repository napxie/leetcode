import random
class Solution:
    def canPermutePalindrome(self, s: str) -> bool:
        dic = {}
        for i in s:
            dic[i] = dic.get(i, 0) + 1
        odd = 0
        for v in dic.values():
            if v % 2 == 1:
                odd += 1
        if odd > 1:
            return False
        return True


if __name__ == "__main__":
    s = "tactcoa"
    print(Solution().canPermutePalindrome(s))
