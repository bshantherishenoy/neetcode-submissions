"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        map_graph = {}
        def dfs(node,map_graph):
            if node == None:
                return 
            if node.val in map_graph:
                return map_graph[node.val]

            clone = Node(node.val)
            map_graph[node.val] = clone

            for neighbor in node.neighbors:
                clone.neighbors.append(dfs(neighbor, map_graph))

            return clone
        return dfs(node, map_graph)
        