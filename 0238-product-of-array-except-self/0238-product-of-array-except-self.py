class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        answer = [1]*n
        #answer = [1,1,1,1]
        for i in range(1,n):
            answer[i] = answer[i-1]*nums[i-1]
            # nums = [1,2,3,4]
            # answer[1] = answer[0]*nums[0]
            # answer[1] = 1*1 = 1
            # answer [2] = 1*2 = 2
            # answer [3] = 2*3 = 6
            # answer = [1,1,2,6]
        right_product = 1
        for i in range (n-1,-1,-1): # (3,2,1) 
            answer[i] *= right_product
            #answer[3]= 6*1 =6
            #answer[2]= 2*4 =8
            #answer[1]= 1*12 = 12
            #answer[0]= 1*24 = 24
            right_product *= nums[i]
            # right_product = 1*4 = 4
            # right_product = 4*3 = 12
            # right_product = 12*2 = 24
            # right_product = 24*1 = 24
        return answer 
        





        







        