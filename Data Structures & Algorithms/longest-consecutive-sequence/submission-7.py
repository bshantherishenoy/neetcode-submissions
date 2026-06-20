class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # this is nlogn approch where we sort and remove the dupes 
        # check with the previous if the differnce is 1 then increase it to 1.
        # by default [2] has a difference of 1
        # if the list is empty then return 0 
        if not nums:
            return 0
        nums = sorted(set(nums))
        max_count = 1 
        count = 1 
        for j in range(1, len(nums)):
            if nums[j]  == nums[j-1] + 1:
                count +=1
            else:
                count = 1
            max_count = max(max_count, count)
        return max_count
        