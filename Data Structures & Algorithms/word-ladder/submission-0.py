class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0
        def regex_match(word):
            result = []
            for i in range(len(word)):
                tfword = word[:i] + "*" + word[i+1:]
                result.append(tfword)
            return result 
        graph = {}
        wordList.append(beginWord)
        for word in wordList:
            result = regex_match(word)
            for k in result:
                if k in graph:
                    graph[k].append(word)
                else:
                    graph[k] = [word]
        wordList.pop()
        visited = set()
        visited.add(beginWord)
        steps = 1
        queue = [beginWord]

        while queue:
            for _ in range(len(queue)):
                word = queue.pop(0)
                if word == endWord:
                    return steps
                for pattern in regex_match(word):
                    for nei in graph.get(pattern, []):
                        if nei not in visited:
                            visited.add(nei)
                            queue.append(nei)
            steps += 1

        return 0