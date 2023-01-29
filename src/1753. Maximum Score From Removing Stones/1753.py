class Solution:
    def maximumScore(self, a: int, b: int, c: int) -> int:
        s = a + b + c
        max_val = max(a, b, c)
        if s < max_val * 2:
            return s - max_val
        else:
            return s // 2
        # return s - max_val if s < max_val * 2 else s // 2

if __name__ == '__main__':
    a = 2
    b = 4
    c = 6
    print(Solution().maximumScore(a, b, c))