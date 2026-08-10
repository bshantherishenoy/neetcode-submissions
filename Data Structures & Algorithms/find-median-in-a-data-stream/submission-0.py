import heapq
class MedianFinder:

    def __init__(self):
        self.small = []
        self.large = []
        

    def addNum(self, num: int) -> None:
        # you add a num first to small
        heapq.heappush(self.small,-num)
        # check if num in small is larger then small of larger then you add to large
        if self.large and -self.small[0] > self.large[0]:
            num = heapq.heappop(self.small)
            heapq.heappush(self.large,-num)

        # check if num of small > len(large)+1
        if len(self.small) > len(self.large) + 1:
            num = -heapq.heappop(self.small)
            heapq.heappush(self.large,num)
        # check if num of large >len of small
        elif len(self.large) > len(self.small):
            num = heapq.heappop(self.large)
            heapq.heappush(self.small,-num)

    def findMedian(self) -> float:
        if len(self.small) > len(self.large):
            return -self.small[0]
        else:
            return (-self.small[0] + self.large[0])/2
        
        