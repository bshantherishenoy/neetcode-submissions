class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        parent = [i for i in range(len(edges)+1)]
        def find(node):
            if parent[node] == node:
                return node
            parent[node] = find(parent[node])
            return parent[node]
        for e, v in edges:
            root_u = find(e)
            root_v = find(v)
            if root_u == root_v:
                return [e,v]
            parent[root_v] = root_u