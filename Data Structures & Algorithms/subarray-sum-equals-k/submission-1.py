class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        # ask the same question to chatgpt and tell him to do  it 
        # in interactive mode , it explains you beautifully 
        hm = {0:1} #why this is needed ,probably we saw zero
        prefix = 0
        count = 0
        for num in nums:
            prefix +=num # add the current prefix
            need = prefix -k # we see a zero here usually  
            count += hm.get(need,0) #  check if the pprefix was already present 
            hm[prefix] = hm.get(prefix,0) + 1 # if the perfix was found update it 
        return count
        """
        I never thought I can approch this problem , I was always giving n^2 solution 
        which I thought was sane , if you see it carefully prefix is a good pattern 
        when ever you see [1]//1 , [1,2] //3, [1,2,3]//6 the sum equivalent of the prefixes
        you could see that a sum [2,3] //5 could be made using 6-1 prefix diff
        we might need current-prefix - num persent in the prefix hashmap and check the prefixes.        
        """

        