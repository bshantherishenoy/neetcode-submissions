class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows = len(board)
        cols = len(board[0])

        def isvalid(r,c,i) -> bool:
            print(r,c,i)
            if 0<= r < rows and 0<=c<cols and board[r][c] != 'X' and board[r][c] == word[i]:
                return True
            else:
                return False
        
        def dfs(r,c,i) -> bool:
            nonlocal board
            if i == len(word):
                return True
            if isvalid(r,c,i):
                temp = board[r][c]
                board[r][c] = "X"
                found =( 
                dfs(r+1, c, i+1) or
                dfs(r,c+1, i+1) or
                dfs(r-1,c,i+1) or
                dfs(r,c-1,i+1)
                )
                board[r][c] = temp
                return found

            else:
                return False

        for i in range(rows):
            for j in range(cols):
                if board[i][j] == word[0]:
                    if dfs(i,j,0):
                        return True
        return False




        