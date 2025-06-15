class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        idx = -1

        # Step 1: Find the first decreasing element from the back
        for i in range(n - 2, -1, -1):
            if nums[i] < nums[i + 1]:
                idx = i
                break

        if idx == -1:
            # Step 2: If no such index, reverse entire array
            nums.reverse()
            return

        # Step 3: Find the next greater element on right of idx
        for i in range(n - 1, idx, -1):
            if nums[i] > nums[idx]:
                nums[i], nums[idx] = nums[idx], nums[i]
                break

        # Step 4: Reverse the suffix starting at idx + 1
        nums[idx + 1 :] = reversed(nums[idx + 1 :])
