class Solution:
    def reverseOnlyLetters(self, S: str) -> str:
        ans = []
        j = -1
        for i, x in enumerate(S):
            if x.isalpha():
                while not S[j].isalpha():
                    j -= 1
                ans.append(S[j])
                j -= 1
            else:
                ans.append(x)
        return "".join(ans)

if __name__ == "__main__":
    S = "ab-cd"
    print(Solution().reverseOnlyLetters(S))