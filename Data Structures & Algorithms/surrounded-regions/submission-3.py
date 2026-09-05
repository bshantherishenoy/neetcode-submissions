class Solution:
    def solve(self, board: List[List[str]]) -> None:
        row = len(board)
        col = len(board[0])
        queue = []
        # get the border 0 
        # Put all border O's into the queue
        for r in range(row):
            if board[r][0] == "O":
                queue.append((r, 0))
                board[r][0] = "S"

            if board[r][col - 1] == "O":
                queue.append((r, col - 1))
                board[r][col - 1] = "S"

        for c in range(col):
            if board[0][c] == "O":
                queue.append((0, c))
                board[0][c] = "S"

            if board[row - 1][c] == "O":
                queue.append((row - 1, c))
                board[row - 1][c] = "S"

        directions = [
            (1, 0),
            (-1, 0),
            (0, 1),
            (0, -1)
        ]
        while queue:
            r,c  = queue.pop(0)
            for dr,dc in directions:
                nr = r + dr
                nc = c + dc
                if 0<=nr<row and 0<=nc<col and board[nr][nc] == "O":
                    queue.append((nr,nc))
                    board[nr][nc] = "S"
        for i in range(row):
            for j in range(col):
                if board[i][j] == "O":
                    board[i][j] = "X"

                elif board[i][j] == "S":
                    board[i][j] = "O"
        

