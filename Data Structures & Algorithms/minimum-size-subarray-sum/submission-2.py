class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        left = 0 
        min_count = 10000
        current_sum = 0
        for right in range(len(nums)):
            current_sum += nums[right]
            while current_sum >= target:
                min_count = min(min_count ,right-left+1)
                current_sum -= nums[left]
                left +=1
        if min_count == 10000:
            return 0
        return min_count    
        