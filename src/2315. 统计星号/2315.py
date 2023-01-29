class Solution:
    def countAsterisks(self, s: str) -> int:
        res, counts = 0, 0
        for i in s:
            if i == "|":
                counts += 1
            elif i == "*" and counts % 2 == 0:
                res += 1
        return res
    
if __name__ == "__main__":
    s = "l|*e*et|c**o|*de|"
    print(Solution().countAsterisks(s))
