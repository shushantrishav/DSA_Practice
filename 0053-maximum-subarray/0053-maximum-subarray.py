class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxsum = float('-inf')
        currentsum = 0
        for ele in nums:
            currentsum = max(ele, currentsum + ele)
            maxsum = max(maxsum, currentsum)
        return maxsum