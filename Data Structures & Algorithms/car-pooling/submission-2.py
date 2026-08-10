import heapq
class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        heap = []
        count = 0
        trips.sort(key=lambda x:x[1])
        # use the min heap for the lowest distance to the east
        for c,f,t in trips:
            while heap and heap[0][0] <=f:
                tot,coc = heapq.heappop(heap)
                count -=coc
            count += c
            if count > capacity:
                return False
            heapq.heappush(heap,(t,c))
        return True

        