class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        max_area = 0
       
        for i in range(len(heights)):
            min_height = float('inf')
            for j in range(i, len(heights)):
                min_height = min(min_height, heights[j])
                area = (j - i + 1) * min_height
                max_area = max(max_area, area)
        return max_area
        