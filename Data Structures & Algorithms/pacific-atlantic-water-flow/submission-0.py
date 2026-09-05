class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        row = len(heights)
        col = len(heights[0])

        pacific = set()
        atlantic = set()
        directions = [
            (0,1),
            (0,-1),
            (1,0),
            (-1,0)
        ]
        def dfs(r, c, visited):
            if not (0<=r<row and 0<=c<col):
                return 
            if (r,c) in visited:
                return 
            visited.add((r,c))
            for  dr,dc in directions:
                nx = r + dr
                nc = c + dc
                if 0 <= nx < row and 0 <= nc < col and heights[nx][nc] >= heights[r][c]:
                    dfs(nx, nc, visited)
        # Pacific: top row + left column
        for c in range(col):
            dfs(0, c, pacific)

        for r in range(row):
            dfs(r, 0, pacific)

        # Atlantic: bottom row + right column
        for c in range(col):
            dfs(row - 1, c, atlantic)

        for r in range(row):
            dfs(r, col - 1, atlantic)

        # Cells reachable from both oceans
        result = []

        for r in range(row):
            for c in range(col):
                if (r, c) in pacific and (r, c) in atlantic:
                    result.append([r, c])

        return result

        