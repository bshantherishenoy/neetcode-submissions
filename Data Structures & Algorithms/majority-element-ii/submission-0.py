class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        # get the 2 candidates that can occur the most number of time 
        res = []
        candidate_1 = None 
        candidate_2 = None
        count1 = 0 
        count2 = 0 
        for num in nums:
            if num == candidate_1:
                count1 +=1
            elif num == candidate_2:
                count2 +=1
            elif count1 == 0:
                candidate_1 = num
                count1 = 1
            elif count2 == 0:
                candidate_2 = num
                count2 = 1
            else:
                count1 -= 1
                count2 -= 1
        # after getting the candidates get their actual count 
        count1 = 0 
        count2 = 0 
        for num in nums:
            if num == candidate_1:
                count1+=1
            elif num == candidate_2:
                count2 += 1
        n = len(nums)
        if count1 > n//3:
            res.append(candidate_1)
        if count2 > n//3:
            res.append(candidate_2)
        
        return res
        