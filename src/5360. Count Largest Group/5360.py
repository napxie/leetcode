class Solution:
    def countLargestGroup1(self, n: int) -> int:
        if n <= 9:
            return n
        dic = {}
        for i in range(1, n+1):
            s = 0
            for j in str(i):
                s += int(j)
            dic[s] = dic.get(s, 0) + 1
        for value in dic.values():
            dic1[value] = dic1.get(value, 0) + value
        a = sorted(dic1.keys())
        return dic1[a[-1]] // a[-1]

    def countLargestGroup(self, n: int) -> int:
        if n <= 9:
            return n
        dic, dic1, maxlen = {}, {}, 0
        for i in range(1, n+1):
            s = 0
            for j in str(i):
                s += int(j)
            dic[s] = dic.get(s, 0) + 1
        dic = sorted(dic.items(), key=lambda k: k[1], reverse=True)
        res = 1
        for i in range(1, len(dic)):
            if dic[i][1] == dic[0][1]:
                res += 1
            else:
                break
        return res


if __name__ == "__main__":
    n = 31
    print(Solution().countLargestGroup(n))
