class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        nums = sorted(set(nums))
        max_count = 1 
        count = 1 
        for j in range(1, len(nums)):
            if nums[j] - nums[j-1] == 1:
                count +=1
            else:
                count = 1
            max_count = max(max_count, count)
        return max_count
        