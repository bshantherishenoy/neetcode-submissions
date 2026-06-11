class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        if len(nums) <=1:
            return nums
        def merge_sort(left, right):
            res = []
            i = 0
            j = 0 
            while i<len(left) and j< len(right):
                if left[i] <= right[j]:
                    res.append(left[i])
                    i+=1
                elif left[i] > right[j]:
                    res.append(right[j])
                    j+=1
            if i < len(left):
                res.extend(left[i:])
            if j < len(right):
                res.extend(right[j:])
            return res
        mid = len(nums)//2
        left = self.sortArray(nums[:mid])
        right = self.sortArray(nums[mid:])
        return merge_sort(left,right)