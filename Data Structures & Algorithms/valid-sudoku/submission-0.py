class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row_set = [ set() for i in range(9)]
        col_set = [set() for j in range(9)]
        box_set = [set() for k in range(9)]

        for r in range(len(board)):
            for c in range(len(board)):
                val = board[r][c]
                if val == ".":
                    continue 
                box = ((r//3) * 3) + (c//3)
                if val in row_set[r] or val in col_set[c] or val in box_set[box]:
                    return False
                row_set[r].add(val)
                col_set[c].add(val)
                box_set[box].add(val)
        return True