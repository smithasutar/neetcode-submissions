class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        last = len(matrix[0])-1
        
        t = 0
        b = len(matrix)-1
        while t <= b:
            m = (t+b)//2
            if matrix[m][-1] < target:
                t = m+1
            elif matrix[m][0] > target:
                b = m-1
            else:
                break
        if t > b:
            return False

        row = m

        l = 0
        r = last
        while l <= r:
            m = (l+r)//2
            if matrix[row][m] == target:
                return True
            if matrix[row][m] < target:
                l = m+1
            if matrix[row][m] > target:
                r = m-1
        return False

        