class Solution:
    def buildMatrix(self, k: int, rowConditions: List[List[int]], colConditions: List[List[int]]) -> List[List[int]]:
        row = {}
        col = {}

        # Create all nodes
        for i in range(1, k + 1):
            row[i] = set()
            col[i] = set()

        # Build row graph
        for r1, r2 in rowConditions:
            row[r1].add(r2)

        # Build column graph
        for c1, c2 in colConditions:
            col[c1].add(c2)

        # Topological sort
        def topological_sort(graph):
            result = []
            visited = set()
            path = []

            def dfs(node):

                if node in path:
                    return False

                if node in visited:
                    return True

                path.append(node)

                for nei in graph[node]:
                    if not dfs(nei):
                        return False

                path.remove(node)
                visited.add(node)
                result.append(node)

                return True

            for node in graph:
                if node not in visited:
                    if not dfs(node):
                        return []

            return result[::-1]

        # Get row order
        actual_rows = topological_sort(row)

        if not actual_rows:
            return []

        # Get column order
        actual_col = topological_sort(col)

        if not actual_col:
            return []

        # Create matrix
        matrix = [[0 for _ in range(k)] for _ in range(k)]

        # Store position of each number
        row_position = {}
        col_position = {}

        for i in range(k):
            row_position[actual_rows[i]] = i
            col_position[actual_col[i]] = i

        # Put numbers in matrix
        for num in range(1, k + 1):
            r = row_position[num]
            c = col_position[num]

            matrix[r][c] = num

        return matrix