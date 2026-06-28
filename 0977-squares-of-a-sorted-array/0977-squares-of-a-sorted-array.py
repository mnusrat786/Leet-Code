class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        nums1= [i*i for i in nums]
        nums1.sort()
        return nums1  

        