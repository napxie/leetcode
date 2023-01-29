class Solution:
    def isSameAfterReversals(self, num: int) -> bool:
        s1 = int(str(num)[::-1], base=10)
        s2 = int(str(s1)[::-1], base=10)
        if num == s2:
            return True
        else:
            return False


        
if __name__ == "__main__":
    num = 1800
    print(Solution().isSameAfterReversals(num))