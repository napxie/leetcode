class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        s, lens = list(s), len(s)
        for i in range(0, lens, 2 * k):
            left = i
            right = min(left+k-1, lens-1)
            while left < right:
                s[right], s[left] = s[left], s[right]
                left += 1
                right -= 1
        return ''.join(s)


if __name__ == "__main__":
    s, k = "abcdefg", 2
    print(Solution().reverseStr(s, k))
