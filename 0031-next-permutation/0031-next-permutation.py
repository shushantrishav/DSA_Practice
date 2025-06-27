class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        rows = len(nums)
        idx_dec = -1

        # Step 1: Find the first decreasing element from the back
        for idx in range(rows - 2, -1, -1):
            if nums[idx] < nums[idx + 1]:
                idx_dec = idx
                break
        # Step 2: If no such index, reverse entire array
        if idx_dec == -1:
            nums.reverse()
            return
        # Step 3: Find the next greater element on right of idx
        for idx in range(rows - 1, idx_dec, -1):
            if nums[idx] > nums[idx_dec]:
                nums[idx], nums[idx_dec] = nums[idx_dec], nums[idx]
                break

        # Step 4: Reverse the suffix starting at idx + 1
        nums[idx_dec + 1 :] = reversed(nums[idx_dec + 1 :])
