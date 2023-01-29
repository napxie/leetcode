from typing import List
class Solution:
    def executeInstructions(self, n: int, startPos: List[int], s: str) -> List[int]:
        m = len(s)
        l = list(s)
        answer = []
        
        for i in range(m):
            answer.append(0)
            startrow, startcol = startPos[0], startPos[1]
            for j in l[i::]:
                if j == "L" and startcol != 0:
                    startcol -= 1
                elif j == "R" and startcol != n-1:
                    startcol += 1
                elif j == "U" and startrow != 0:
                    startrow -= 1
                elif j == "D" and startrow != n-1:
                    startrow += 1
                else:
                    break
                answer[i] += 1
                
        return answer
if __name__ == "__main__":
    n = 3 
    startPos = [0,1]
    s = "RRDDLU"
    print(Solution().executeInstructions(n, startPos, s))
                    

