class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        n = len(grid)

        # (water_level_needed, row, col)
        heap = [(grid[0][0], 0, 0)]

        visited = set()

        while heap:
            water, r, c = heapq.heappop(heap)

            if (r, c) in visited:
                continue

            visited.add((r, c))

            # Reached bottom-right
            if r == n - 1 and c == n - 1:
                return water

            # Move up, down, left, right
            directions = [
                (1, 0),
                (-1, 0),
                (0, 1),
                (0, -1)
            ]

            for dr, dc in directions:
                nr = r + dr
                nc = c + dc

                if 0 <= nr < n and 0 <= nc < n:
                    if (nr, nc) not in visited:

                        # Water must be high enough for BOTH:
                        # current path and the new cell
                        new_water = max(water, grid[nr][nc])

                        heapq.heappush(
                            heap,
                            (new_water, nr, nc)
                        )
        