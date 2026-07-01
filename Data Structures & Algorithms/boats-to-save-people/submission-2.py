class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        n = len(people)
        people.sort() # greedy way to sort the people based on their weight
        left = 0 
        right = n - 1
        count = 0 
        while left <= right: 
            sumz = people[left] + people[right]
            if sumz == limit:
                count +=1
                left +=1
                right -=1
            elif sumz > limit:
                right -=1 
                count +=1
            else : 
                left +=1  
                right -=1
                count +=1
        return count