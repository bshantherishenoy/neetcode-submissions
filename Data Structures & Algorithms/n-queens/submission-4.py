class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        result = []
        graph = [["."] * n for _ in range(n)]
        def check(row, col , graph):
            # check the current row
            for r in range(row):
                if graph[r][col] == "Q":
                    return False
            # check the left diagonal
            r = row -1
            c = col -1
            while r>=0 and c>=0:
                if graph[r][c] == "Q":
                    return False
                r -=1
                c -=1
            r = row - 1
            c = col + 1 
            while r>=0 and c<n:
                if graph[r][c] == "Q":
                    return False
                r -=1
                c +=1
            return True

        def backtrack(index, graph):
            if index == n:
                result.append(["".join(r) for r in graph])
                return
            for col in range(n):
                if check(index, col , graph):
                    graph[index][col] = "Q"
                    backtrack(index+1,graph)
                    graph[index][col] = "."
        backtrack(0, graph)
        return result