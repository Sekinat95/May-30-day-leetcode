class Solution:
    def firstUniqChar(self, s: str) -> int:
        dict = {}
        result = []
        for i in s:
            if i not in dict:
                dict[i] = 1
            else:
                dict[i] += 1
        for i in dict:
            if dict[i] == 1:
                result.append(i)
        if not result:
            return -1
        else:
            return s.index(result[0])