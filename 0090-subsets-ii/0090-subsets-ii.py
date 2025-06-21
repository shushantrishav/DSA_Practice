class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        def DFS(start, subset):
            result.append(subset[:])

            for i in range(start, len(nums)):
                # Skip duplicates at the same recursion depth
                if i > start and nums[i] == nums[i-1]:
                    continue

                subset.append(nums[i])
                DFS(i + 1, subset)
                subset.pop()  # DFS

        nums.sort()
        result = []
        DFS(0, [])
        return result
