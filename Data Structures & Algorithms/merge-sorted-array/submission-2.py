class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        k = len(nums1)
        zero = abs(k-m)
        for i in range(zero):
            nums1.append(nums2[i])
            nums1.remove(0)
        nums1.sort()
        return nums1