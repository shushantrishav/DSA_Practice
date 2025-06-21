class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        def solve(index, subset):
            if index == len(nums):
                result.append(subset[:])
                return

            # Include nums[index]
            subset.append(nums[index])
            solve(index + 1, subset)
            subset.pop()  # Backtrack

            # Skip duplicates when excluding
            next_index = index + 1
            while next_index < len(nums) and nums[next_index] == nums[index]:
                next_index += 1

            # Exclude nums[index] and all its duplicates
            solve(next_index, subset)

        nums.sort()  # Sort to handle duplicates
        result = []
        solve(0, [])
        return result
