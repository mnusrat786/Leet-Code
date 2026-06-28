class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        # nums1 = [i*i for i in nums]
        nums1=[]
        for i in nums:
           i = i*i
           nums1.append(i)
           nums1.sort()
        return nums1
        # nums1.sort()
        # return nums1