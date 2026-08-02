"""
# Definition for a QuadTree node.
class Node:
    def __init__(self, val, isLeaf, topLeft, topRight, bottomLeft, bottomRight):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight
"""

class Solution:
    def construct(self, grid: List[List[int]]) -> 'Node':
        def builder(r,c,size):
            first = grid[r][c]
            for i in range(r,r+size):
                for j in range(c,c+size):
                    if grid[i][j] != first:
                        half = size//2
                        tl = builder(r,c,half)
                        tr = builder(r,c+half,half)
                        bl = builder(r+half,c,half)
                        br = builder(r+half,c+half,half)
                        return Node(
                                val=True,
                                isLeaf=False,
                                topLeft=tl,
                                topRight=tr,
                                bottomLeft=bl,
                                bottomRight=br
                                )
                    
            return Node(
                    val=(first == 1),
                    isLeaf=True,
                    topLeft=None,
                    topRight=None,
                    bottomLeft=None,
                    bottomRight=None
                    )
        n = len(grid)
        return builder(0,0,n)

        