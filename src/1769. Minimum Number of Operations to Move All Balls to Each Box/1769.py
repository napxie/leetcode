from typing import List

class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        # 1
        # left, right, operations = int(boxes[0]), 0, 0
        # for i in range(1, len(boxes)):
        #     if boxes[i] == '1':
        #         right += 1
        #         operations += i
        # res = [operations]
        # for i in range(1, len(boxes)):
        #     operations += left - right
        #     if boxes[i] == '1':
        #         left += 1
        #         right -= 1
        #     res.append(operations)
        # return res 
        # 2 
        res = []
        for i in range(len(boxes)):
            s = 0
            for j, c in enumerate(boxes):
                if c == '1':
                   s += abs(j-i)
            res.append(s)
        return res
                   
            

if __name__ == "__main__":
    boxes = "110"
    print(Solution().minOperations(boxes))
