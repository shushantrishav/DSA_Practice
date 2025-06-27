class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        low = 0
        swap = 0
        high = len(nums) - 1
        while(swap <= high):
            if (nums[swap] == 0):
                nums[low], nums[swap] = nums[swap], nums[low]
                low += 1
                swap += 1
            elif (nums[swap] == 1):
                swap += 1
            else:
                nums[high], nums[swap] = nums[swap], nums[high]
                high -= 1
        