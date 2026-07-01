class Solution:
    def maxArea(self, heights: List[int]) -> int:
        #very very basic
        #think you are calculating area of rectangle which is 
        #width* height 
        #you need to keep a track of every area , discared the low ones
        #both height and with should be more to get the area
        #you can fight with a guy of your height not taller , can win on lower ofcose
        left = 0
        right = len(heights) - 1
        max_area = 0 

        while left < right:
            width = right-left 
            height = min(heights[left],heights[right])
            area = width * height 
            max_area = max(max_area, area)
            if heights[left] < heights[right]:
                left +=1
            else:
                right -=1
        return max_area

        