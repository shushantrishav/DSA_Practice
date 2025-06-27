class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        indexmap = {}

        for idx in range(0, len(nums)):
            val = nums[idx]
            diff = target - val
            if diff in indexmap:
                return [indexmap[diff], idx]
            else:
                indexmap[val] =  idx

        return [-1,-1]