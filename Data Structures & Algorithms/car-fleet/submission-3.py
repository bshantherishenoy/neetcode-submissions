class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = list(zip(position, speed))
        stack = []
        cars.sort(reverse=True)
        for position,speed in cars:
            time = (target- position) / speed
            if not stack or time > stack[-1]:
                stack.append(time)
        return len(stack)