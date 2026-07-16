class Solution:
    def mySqrt(self, x: int) -> int:
        left = 1
        right = x
        while left <= right:
            mid = (left + right)//2
            print(mid)
            cur_sq = mid * mid
            if cur_sq  == x:
                return mid
            elif cur_sq < x:
                left = mid + 1
            else:
                right = mid -1
        return right
            