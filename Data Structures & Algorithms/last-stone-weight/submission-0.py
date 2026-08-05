import heapq
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        neg_stones = [-i for i in stones]
        heapq.heapify(neg_stones)
        print(neg_stones)
        while len(neg_stones) > 1:
            num1 = heapq.heappop(neg_stones)
            num2 = heapq.heappop(neg_stones)
            print(neg_stones)
            smash = num1 - num2
            heapq.heappush(neg_stones, smash)
            print(neg_stones)
        return -neg_stones[0]
        