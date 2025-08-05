class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        nonzero = []
        for i in nums:
            if i != 0:
                nonzero.append(i)

        while len(nonzero) < len(nums):
            nonzero.append(0)
        nums[:] = nonzero    

        