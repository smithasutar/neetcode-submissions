class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        num_row = len(grid)
        num_col = len(grid[0])
        perm = 0
        visit = set()

        for row in range(num_row):
            for col in range(num_col):
                
                if grid[row][col] == 1:
                    check_up = row+1 
                    if check_up < 0 or check_up >= num_row or grid[check_up][col]==0:
                        perm +=1
                    check_down = row-1 
                    if check_down < 0 or check_down >= num_row or grid[check_down][col]==0:
                        perm +=1
                    check_right = col+1 
                    if check_right < 0 or check_right >= num_col or grid[row][check_right]==0:
                        perm +=1
                    check_left = col-1 
                    if check_left < 0 or check_left >= num_col or grid[row][check_left]==0:
                        perm +=1
                    if (row, col) in visit:
                        perm +=0
                    else:
                        visit.add((row,col))
        return perm