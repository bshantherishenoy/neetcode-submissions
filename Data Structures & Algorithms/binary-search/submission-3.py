class Solution:
    def search(self, nums: List[int], target: int) -> int:
        nums.sort()
        left = 0 
        right = len(nums) 
        while left < right :
            mid = (left +  right )//2 
            if nums[mid] == target:
                return mid
            elif nums[mid] <  target:
                left = mid+1
            else:
                right = mid 
        return -1
        