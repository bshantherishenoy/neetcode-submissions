class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = {}
        for word in strs:
            sorted_word = sorted(word)
            sorted_word = "".join(sorted_word)
            if sorted_word not in anagrams:
                anagrams[sorted_word] = [word]
            else:
                anagrams[sorted_word].append(word)
        return list(anagrams.values())
        