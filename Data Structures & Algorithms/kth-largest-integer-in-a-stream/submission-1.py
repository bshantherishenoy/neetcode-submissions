import heapq
class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.heapz = nums

        heapq.heapify(self.heapz)
        while len(self.heapz) > self.k:
            heapq.heappop(self.heapz)

    def add(self, val: int) -> int:
        heapq.heappush(self.heapz, val)
        if len(self.heapz) > self.k:
            heapq.heappop(self.heapz)
        return self.heapz[0]
        
