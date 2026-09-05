class TrieNode:
    def __init__(self):
        self.children = [None] * 26 
        self.leafNode = False
class WordDictionary:

    def __init__(self):
        self.root = TrieNode()
        

    def addWord(self, word: str) -> None:
        cur = self.root 
        for char in word:
            index = ord(char) - ord("a")
            if cur.children[index] == None:
                cur.children[index] = TrieNode()
            cur = cur.children[index]
        cur.leafNode = True

    def search(self, word: str) -> bool:
        def dfs(node,index):
            if index == len(word):
                return node.leafNode
            char = word[index]
            if char == ".":
                for child in node.children:
                    if child is not None:
                        if dfs(child,index+1):
                            return True
                       
                return False
            index2 = ord(char) - ord("a")
            if node.children[index2] is None:
                return False
            return dfs(node.children[index2], index + 1)
        return dfs(self.root,0)

            
        
