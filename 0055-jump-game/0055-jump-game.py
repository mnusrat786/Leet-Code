class Solution:
    def canJump(self, nums: List[int]) -> bool:
        right = 0
        goal = len(nums)-1       
        for i in range(len(nums)):
            if i > right:
                return False
            if i + nums[i] > right:
                right = nums[i]+i
            if right >= goal:
                return True
# nums = [2,3,1,1,4]
# i=0  0!>0  0+2>0  so right = 2
# i=1  1!>2  1+3>2  so right = 4
# i=2  2!>4  2+1!>4  4>=4  True

#  nums = [3,2,1,0,4]
# i = 0  0!>0  0+3>0 so right = 3
# i = 1  1!>3  1+2!>3  3!>=4 
# i = 2  2!>4  2+1!>3  3!>=4
# i=3  3!>3  3+0!>3  3!>=4
# i=4  4>3 return False
            
            