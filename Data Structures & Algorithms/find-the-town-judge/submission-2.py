class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        
        sec = []
        for i in range(len(trust)):
            sec.append(trust[i][1])

        if len(set(sec)) == 1 and n > 1:
            return sec[0]
        return -1