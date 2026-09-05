class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        rank = {}
        count = 0
        for c in order:
            if c not in rank:
                rank[c] = count 
                count +=1
        n = len(words)
        w = 1
        # compare every two words based on the rank 
        def compare(word1:str, word2:str) -> bool:
            l1 = word1
            l2 = word2
            index_1 = 0
            index_2 = 0
            print(word1,word2)
            while index_1 < len(word1) and index_2 < len(word2):
                if rank[word1[index_1]] < rank[word2[index_2]]:
                    return True
                elif rank[word1[index_1]] > rank[word2[index_2]]:
                    return False
                index_1 +=1
                index_2 +=1 
            return len(word1) <= len(word2)
        for w in range(1,n):
            if not compare(words[w-1], words[w]):
                return False
        return True