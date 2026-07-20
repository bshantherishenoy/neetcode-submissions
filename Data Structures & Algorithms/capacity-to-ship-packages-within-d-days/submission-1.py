class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        low= max(weights)
        high=sum(weights)
        while low<high:
            mid= (low+high)//2
            day=1
            cur_load=0
            for weight in weights:
                if cur_load + weight <= mid:
                    cur_load+=weight
                else:
                    cur_load=weight
                    day+=1
            if day <= days:
                high = mid
            else:
                low=mid+1 
        return low 
