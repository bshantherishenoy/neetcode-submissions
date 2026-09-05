from collections import Counter, deque
import heapq
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        # get the number of times the task is executed 
        freq = Counter(tasks)
        heap = [-count for count in freq.values()]
        heapq.heapify(heap)
        # set a cool down and time 
        cooldown = deque()  # (remaining_count, available_time)

        time = 0
        while heap or cooldown:
            time +=1 
            if heap:
                count = heapq.heappop(heap) + 1
                if count != 0:
                    cooldown.append((count, time+n) )

            if cooldown and cooldown[0][1] == time:
                heapq.heappush(heap, cooldown.popleft()[0])
        return time

