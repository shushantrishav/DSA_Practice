class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        maxSum = float('-inf')
        currentSum = 0
        for ele in nums:
            currentSum = max(ele, currentSum + ele)
            maxSum =  max(maxSum, currentSum)
        return maxSum