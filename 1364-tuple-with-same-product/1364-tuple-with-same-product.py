from collections import Counter
class Solution:
    def tupleSameProduct(self, nums: List[int]) -> int:        
        c = Counter()

        for i in range(len(nums)):
            for j in range(i):

                p = nums[i] * nums[j]

                c[p] += 1

        output = 0

        for k in c.values():
            if k>1:                            
                output +=  4*(k *(k-1)) 
        
        return output              
            
            
                




        

        