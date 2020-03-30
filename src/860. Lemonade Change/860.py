from typing import List


class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        five = ten = 0
        for bill in bills:
            if bill == 5:
                five += 1
            elif bill == 10:
                if not five:
                    return False
                five -= 1
                ten += 1
            else:
                if ten and five:
                    five -= 1
                    ten -= 1
                elif five >= 3:
                    five -= 3
                else:
                    return False
        return True


if __name__ == "__main__":
    bills = [5, 5, 5, 10, 20]
    print(Solution().lemonadeChange(bills))
