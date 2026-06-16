class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        number_one = 0
        number_two = 0 
        number_zero = 0
        for i in nums:
            if i == 1:
                number_one+=1
            elif i == 2:
                number_two +=1
            else:
                number_zero+=1
        #replaces the contents of the existing list object, so any references to that list see the updated values.
        nums[:]=  [0]*number_zero + [1] * number_one + [2] *number_two
 