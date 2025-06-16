class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        if not nums:
            return []

        # Initialize candidates and counters
        candidate1, candidate2 = None, None
        count1, count2 = 0, 0

        # First pass: find potential candidates
        for num in nums:
            if num == candidate1:
                count1 += 1
            elif num == candidate2:
                count2 += 1
            elif count1 == 0:
                candidate1, count1 = num, 1
            elif count2 == 0:
                candidate2, count2 = num, 1
            else:
                count1 -= 1
                count2 -= 1

        # Second pass: verify counts
        result = []
        for candidate in [candidate1, candidate2]:
            if nums.count(candidate) > len(nums) // 3:
                result.append(candidate)

        return result
