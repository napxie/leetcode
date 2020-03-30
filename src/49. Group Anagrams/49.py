from typing import List


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dic = {}
        for word in strs:
            cur = str(sorted(word))
            if cur not in dic:
                dic[cur] = [word]
            else:
                dic[cur].append(word)
        res = []
        for key, value in dic.items():
            res.append(value)
        return res

    def groupAnagrams1(self, strs: List[str]) -> List[List[str]]:
        for s in strs:
            count = [0] * 26
            for c in s:
                count[ord(c) - ord('a')] += 1
            ans[tuple(count)].append(s)
        return ans.values()


if __name__ == "__main__":
    strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
    print(Solution().groupAnagrams(strs))
