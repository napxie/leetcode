class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        hash = {}
        for i, c in enumerate(s):
            if hash.get(c):
                if t[i] != hash[c]:
                    return False
            else:
                if t[i] in hash.values():
                    return False
                hash[c] = t[i]
        return True

if __name__ == "__main__":
    s, t =  "egg", "add"
    print(Solution().isIsomorphic(s, t))
