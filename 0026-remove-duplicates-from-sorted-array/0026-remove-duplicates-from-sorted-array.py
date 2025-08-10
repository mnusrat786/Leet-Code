class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        for i in range(len(nums)):                 # i = 0..original_len-1
            for j in range(len(nums)-1, i, -1):    # j goes last -> i+1
                if nums[j] == nums[i]:             # compare to current pivot
                    nums.pop(j)                    # remove duplicate by index
        return len(nums)                           # final count of uniques
