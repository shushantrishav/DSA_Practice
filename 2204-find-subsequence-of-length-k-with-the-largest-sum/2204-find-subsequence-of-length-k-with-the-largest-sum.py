class Solution:
    def maxSubsequence(self, nums: List[int], k: int) -> List[int]:
        # Pair numbers with their indices
        pairs = [(num, i) for i, num in enumerate(nums)]
        
        # Get k largest elements by value
        top_k = heapq.nlargest(k, pairs, key=lambda x: x[0])

        # Sort selected k elements by their original indices to preserve order
        top_k.sort(key=lambda x: x[1])

        # Extract the numbers only
        return [num for num, i in top_k]