class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        # use the array as it own hash map 
        #  @ 0 th position we 
        i = 0 
        n = len(nums)
        while i < n :
            correct = nums[i] - 1
            if 1<= nums[i] <= n and nums[i] != nums[correct]:
                nums[i], nums[correct] = nums[correct], nums[i]
            else:
                i+=1
        for i in range(len(nums)):
            if i+1 != nums[i]:
                return i+1
        return n+1 