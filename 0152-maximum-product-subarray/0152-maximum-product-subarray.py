class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        max_prod = min_prod = result = nums[0]

        for num in nums[1:]:
            if num < 0:
                max_prod, min_prod = min_prod, max_prod  # Swap on negative

            max_prod = max(num, num * max_prod)
            min_prod = min(num, num * min_prod)

            result = max(result, max_prod)

        return result