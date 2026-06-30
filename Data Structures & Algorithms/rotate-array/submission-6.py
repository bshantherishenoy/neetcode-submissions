class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # if the length is greater than the give length.
        n = len(nums) - 1
        k %= len(nums)

        def reverse(left, right):
            while left < right:
                nums[left], nums[right] = nums[right],nums[left]
                left +=1
                right-=1
        reverse(0, n)
        reverse(0,k-1)
        reverse(k,n)

        

     
        