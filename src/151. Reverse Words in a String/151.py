class Solution:
    def reverseWords(self, s: str) -> str:
        s = s + " "
        stack, res = [], ""
        for i in s:
            stack.append(i)
            if i == " ":
                while stack:
                    res = res + stack.pop()
        return res[1:]

if __name__ == "__main__":
    s =  "Let's take LeetCode contest"
    print(Solution().reverseWords(s))