class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        remove_dupe = list(set(nums))
        remove_dupe.sort()
        max_count = 1 
        count = 1 
        i = 0
        nums = remove_dupe
        for j in range(1, len(nums)):
            if nums[j] - nums[i] == 1:
                count +=1
            else:
                count = 1
            i+=1
            max_count = max(max_count, count)
        return max_count
        