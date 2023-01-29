from typing import List

class Solution:
    def finalValueAfterOperations(self, operations: List[str]) -> int:
        sum = 0
        for op in operations:
            if op[1] == '+':
                sum += 1
            else:
                sum -= 1
        return sum
        return sum(1 if op[1] == '+' else -1 for op in operations)
        
if __name__ == "__main__":
    operations = ["--X","X++","X++"]
    print(Solution().finalValueAfterOperations(operations))