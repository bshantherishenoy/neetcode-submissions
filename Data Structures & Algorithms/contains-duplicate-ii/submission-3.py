class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        # Remove the item from a particular index 
        window  = set()
        for i in range(len(nums)):
            if window and len(window) > k:
                window.remove(nums[i-k-1])  
            if nums[i] in window:
                return True
            window.add(nums[i])
        return False