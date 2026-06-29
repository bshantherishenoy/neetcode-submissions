class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # its a sorted array
        # what do we want we want sum of 2
        # we cannot use map well we do not need
        # when ever we see sorted array we think of 2 pointers BS
        l = 0
        r = len(nums)-1
        while l<r:
            sum_lr = nums[l] + nums[r]
            if sum_lr == target:
                return [l+1,r+1]
            elif sum_lr < target:
                l+=1
            else:
                r-=1
        return []