import collections


class Solution:
    def firstUniqChar(self, s: str) -> int:
        count = collections.Counter(s)
        # count = {}
        # for i in s:
        #     count[i] = count.get(i, 0) + 1
        for i, ch in enumerate(s):
            if count[ch] == 1:
                return i
        return -1


if __name__ == "__main__":
    s = "leetcode"
    print(Solution().firstUniqChar(s))
