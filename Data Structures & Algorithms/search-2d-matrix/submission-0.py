class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        last = len(matrix[0])-1
        row = -1

        for i in range(len(matrix)):
            r = matrix[i]
            if r[0] <= target and target <= r[last]:
                row = i
        if row == -1:
            return False
        print(row)
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

        