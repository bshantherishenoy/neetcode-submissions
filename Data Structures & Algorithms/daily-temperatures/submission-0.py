class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        result = [0] * len(temperatures) 
        for i in range(len(temperatures)):
            for j in range(i,len(temperatures)):
                if  i == j:
                    continue 
                else :
                    if temperatures[i] < temperatures[j]:
                         result[i] = j -i 
                         break
        return result
        