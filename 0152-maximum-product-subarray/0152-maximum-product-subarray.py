class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        maximum_product = float("-inf")
        current_product = 1
        for i in nums:
            current_product = current_product * i
            maximum_product = max(maximum_product,current_product)
            if current_product == 0:
                current_product = 1

        current_product = 1
        for i in reversed(nums):
            current_product = current_product*i
            maximum_product = max(maximum_product,current_product)
            if current_product ==0:
                current_product = 1
        return maximum_product        
        
        # nums = [2,3,-2,4]    
        # i = 0,1,2,3    
        # cp = 1*2 = 2  mp= max(-inf,2) = 2
        # cp = 2*3= 6   mp = max(2,6) = 6
        # cp = 6*-2= -12 mp = max(6,-12)=6
        # cp = -12*4 = -48  mp= max(6,-48) = 6

        # nums = [0,1,4]
        # i= 0,1,2
        #cp = 1*0 = 0  mp= max(-inf,0)=0
        #cp= 0*1 = 0  mp= max(0,0) = 0
        #cp = 0*4 = 0  mp= max(0,0)= 0

        # nums = [3,-1,4]
        # i =0,1,2
        #cp= 1*3 = 3  mp =max(-inf,3)= 3
        # cp= 3*-1 = -3 mp= max(3,-3)= 3
        # cp = -3*4=-12 mp=max(3,-12)=3






        