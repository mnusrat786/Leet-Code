class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        current_sum = nums[0]
        max_sum = nums[0]
        for i in range(1,len(nums)):
            current_sum = max(current_sum + nums[i], nums[i])
            # current_sum = max(-2+1,1) = max(-1,1) = 1
            # current_sum = max(1-3,-3) = max(-2,-3) = -2
            # current_sum = max(-2+4,4) = 4
            # current_sum = max(4-1,-1) =3

            max_sum = max(current_sum, max_sum)
            # max_sum = max(1,-2)= 1
            # max_sum = max(-2,1) = 1
            # max_sum = max(4,1) = 4
            # max_sum = max(3,4)= 4
        return max_sum    

        # nums = [-2,1,-3,4,-1,2,1,-5,4]





            


            

        