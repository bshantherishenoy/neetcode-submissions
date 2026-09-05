class Solution:
    def makesquare(self, matchsticks: List[int]) -> bool:
        if sum(matchsticks)%4 == 0:
            # If we can divide by all of them 
            length = sum(matchsticks)//4 
            result = [0]*4 # representing the 4 sides of the square
            if max(matchsticks) > length:
                return False
            def btk(index,sqf):
                if index == len(matchsticks):
                    return sqf[0] == sqf[1] == sqf[2] == sqf[3]
                for i in range(4):
                    if sqf[i] + matchsticks[index] > length:
                        continue
                    sqf[i] += matchsticks[index]
                    if btk(index+1,sqf):
                        return True
                    sqf[i] -= matchsticks[index]
                return False
            return btk(0,[0]*4)
            
        else:
            return False