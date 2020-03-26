from typing import List
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        # res = ""
        # for tmp in zip(*strs):
        #     tmp_set = set(tmp)
        #     if len(tmp_set) == 1:
        #         res += tmp[0]
        #     else:
        #         break
        # return res

        if not strs: return ""
        strs.sort()
        n, res, a, b = len(strs), "", strs[0], strs[len(strs)-1]
        for i in range(len(a)):
            if i < len(b) and a[i] == b[i]:
                res += a[i]
            else:
                break
        return res

if __name__ == "__main__":
    strs = ["flower","flow","flight"]
    print(Solution().longestCommonPrefix(strs))