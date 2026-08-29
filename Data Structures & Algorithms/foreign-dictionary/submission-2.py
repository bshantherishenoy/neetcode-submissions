class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        # Step 1 : Check each words if they have things in common 
        graph = {}
        n = len(words)
        for word in words:
            for char in word:
                if char not in graph:
                    graph[char] = set()
        for i in range(1, len(words)):
            a = words[i-1]
            b = words[i]
            n1 = len(a)
            n2 = len(b)
            j = 0 
            k = 0
            while j<n1 and k<n2:
                if a[j] != b[k]:
                    graph[a[j]].add(b[k])
                    break
                j+=1
                k+=1 
            # Invalid prefix case
            if n1 > n2 and j == n2:
                return ""
        result = ""
        visited = set()
        path = []
        def dfs(node):
            nonlocal result,path
            if node in path:
                return False
            if node  in visited:
                return True

            path.append(node)

            for neg in graph.get(node, []):
                if not dfs(neg):
                    return False
            path.remove(node)
            visited.add(node)
            result += node
            return True
        for key, value in graph.items():
            if key not in visited:
                if not dfs(key):
                    return ""
        return result[::-1]