class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        current_sum = maximum_sum = nums[0]
        for i in range(1,len(nums)):
            current_sum = max(current_sum+nums[i], nums[i])
            maximum_sum = max(current_sum,maximum_sum)
        return maximum_sum
            


            

        