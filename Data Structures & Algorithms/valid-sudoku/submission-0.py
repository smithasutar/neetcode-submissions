class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        for row in range(9):
            row_hash = [0]*10
            for col in range(9):
                if board[row][col] != ".":
                    if int(board[row][col]) > 9 or int(board[row][col]) < 1:
                        return False
                    # print(int(board[row][col]))
                    if row_hash[int(board[row][col])] != 0:
                        return False
                    row_hash[int(board[row][col])] += 1
        
        for col in range(9):
            col_hash = [0]*10
            for row in range(9):
                if board[row][col] != ".":
                    if int(board[row][col]) > 9 or int(board[row][col]) < 1:
                        return False
                    if col_hash[int(board[row][col])] != 0:
                        return False
                    col_hash[int(board[row][col])] += 1

        for box in range(9):
            square_hash = [0] * 10
            box_row = (box // 3) * 3
            box_col = (box % 3) * 3

            for r in range(box_row, box_row + 3):
                for c in range(box_col, box_col + 3):
                    if board[r][c] != ".":
                        num = int(board[r][c])
                        if square_hash[num]:
                            return False
                        square_hash[num] = 1



        return True











