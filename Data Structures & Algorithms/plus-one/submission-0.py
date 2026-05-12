class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        word = ""
        for val in digits:
            word += str(val)
        num = int(word)
        increase = num + 1
        return [int(x) for x in str(increase)]
        
        

