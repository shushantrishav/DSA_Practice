class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        maxOne = 0
        currentOne = 0
        for num in nums:
            if(num == 1):
                currentOne += 1   
            else:
                currentOne = 0
            maxOne = max(maxOne, currentOne)
        return maxOne