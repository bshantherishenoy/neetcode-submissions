class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        # we just start guess if this one is minimum but was thinking to do it by mcm approch
        # did not like to do it this way but lets D when mcm
        # come back with another solution 
        def contains(mid):
            partion = 1
            total = 0
            for ele in nums :
                if total + ele <=mid:
                    total += ele
                else:
                    partion += 1
                    total = ele 
            return partion <= k
        
        
        
        left = max(nums)
        right = sum(nums)
        while left<=right:
            mid  = (left + right)//2
            if contains(mid):
                right = mid -1
            else :
                left = mid + 1
        return left
