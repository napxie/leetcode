class Solution:
    def isFlipedString(self, s1: str, s2: str) -> bool:
        return len(s1) == len(s2) and s1 in s2*2


if __name__ == "__main__":
    s1, s2 = "waterbottle", "erbottlewat"
    print(Solution().isFlipedString(s1, s2))
