class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # if not nums:  # Fixed empty check
        #     return
        
        # Your approach modified to work correctly
        for i in range(len(nums) - 1):  # Fixed: -1 to avoid index error
            for j in range(len(nums) - 1):
                if nums[j] > nums[j + 1]:  # Compare values, not equality
                    # Fixed swap implementation
                    nums[j], nums[j + 1] = nums[j + 1], nums[j]