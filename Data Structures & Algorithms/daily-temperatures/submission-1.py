class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = []
        count = 1 
        for i in range(len(temperatures)):
            j = i+1
            while j < len(temperatures) and temperatures[i] >= temperatures[j]:
                count+=1
                j+=1
            if j >= len(temperatures):
                res.append(0)
            else:  
                res.append(count)
            count = 1

        return res