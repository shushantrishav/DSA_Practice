class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        ans = {}
        for i , num in enumerate(nums):
            complement = target - num
            if complement in ans:
                return [ans[complement], i]
            ans[num] = i