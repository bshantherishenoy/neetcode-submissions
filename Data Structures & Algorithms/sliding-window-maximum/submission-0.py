from collections import deque
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        # using deque to make left, right pops
        # check the next greater element (does the sorting by keeping the top element as max)
        # if it more then window size pop left 
        # if the window size is found then get the top element
        res = []
        d = deque()
        for i in range(len(nums)):
            while d and nums[d[-1]] < nums[i]:
                d.pop()
            d.append(i)
            if d[0] < i-k+1:
                d.popleft()
            if i >= k-1:
                res.append(nums[d[0]])
        return res

        