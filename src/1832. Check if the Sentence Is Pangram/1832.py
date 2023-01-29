class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        state = 0
        for c in sentence:
            state |= 1 << (ord(c) - ord('a'))
        return state == (1 << 26) - 1
    def checkIfPangram1(self, sentence: str) -> bool:
        exist = [False] * 26
        for c in sentence:
            exist[ord(c)-ord('a')] = True 
        return all(exist)

if __name__ == "__main__":
    sentence = "thequickbrownfoxjumpsoverthelazydog"
    print(Solution().checkIfPangram(sentence))