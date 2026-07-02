class Solution:
    def trap(self, height: List[int]) -> int:
        # Baby taught me this 
        # 1.Find the next greater element form left
        # 2.Find the next greater element from right
        # 3.min(le,right) height and then subs with the height
        # add all such areas to get the maximum water filled
        # Step 1:
        n = len(height)
        left_max = [0] * n
        right_max = [0] * n
        left_max[0] = height[0]
        for i in range(1, n):
            left_max[i] = max(left_max[i-1], height[i])
        right_max[-1] = height[-1]
        for j in range(n-2, -1,-1):
            right_max[j] = max(right_max[j+1], height[j])
        sum_arr = 0
        for i in range(n):
            arr = min(left_max[i],right_max[i]) - height[i]
            if arr > 0 :
                sum_arr +=arr
        return sum_arr