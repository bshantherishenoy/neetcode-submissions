import heapq
class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        i = 0
        tasks = [
            (enqueue, process, index)
            for index, (enqueue, process) in enumerate(tasks)
        ]
        tasks.sort()
        ans = []
        heap = []
        time = tasks[0][0]
        
        while len(ans) < len(tasks):
            while i < len(tasks) and tasks[i][0] <= time:
                enqueue, process, index = tasks[i]
                heapq.heappush(heap, (process, index))
                i+=1
            if not heap:
                time =  tasks[i][0]
                continue 
            processing, index = heapq.heappop(heap)
            time += processing
            ans.append(index)
        return ans
        
        