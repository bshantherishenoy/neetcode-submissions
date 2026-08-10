import heapq
class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        heap = []
        for frq, char in [(a,'a'), (b,'b'),(c,'c')]:
            if frq > 0:
                heapq.heappush(heap,(-frq,char))
        ans = ""
        while heap:
            freq, char = heapq.heappop(heap)
            if len(ans) >=2 and ans[-1] == char and ans[-2]==char:
                if not heap:
                    break
                freq2, char2 = heapq.heappop(heap)
                ans += char2
                freq2 += 1
                if freq2 < 0:
                    heapq.heappush(heap ,(freq2, char2))
                heapq.heappush(heap,(freq,char))
            else:
                ans += char
                freq +=1
                if freq<0:
                    heapq.heappush(heap,(freq, char))
        return ans

        