class Solution:
    def isPalindrome(self, s: str) -> bool:
        l, r = 0, len(s)-1
        while l < r:
            if s[l].isalnum() and s[r].isalnum():
                if s[l].upper() == s[r].upper():
                    l, r = l + 1, r - 1
                else:
                    return False
            else:
                if not s[l].isalnum():
                    l += 1
                if not s[r].isalnum():
                    r -= 1
        return True
if __name__ == "__main__":
    s = "A man, a plan, a canal: Panama"
    print(Solution().isPalindrome(s))