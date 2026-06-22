class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        hm = {0:1}
        prefix = 0
        count = 0
        for num in nums:
            prefix +=num 
            need = prefix -k 
            count += hm.get(need,0)
            hm[prefix] = hm.get(prefix,0) +1
        return count

        