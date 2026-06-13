from collections import Counter 
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
       freq = Counter(nums)
       result = sorted(freq, key=lambda x: (freq[x], x),reverse=True)
       return result[:k]



        