class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        mono_q = deque()  # Monotonic decreasing queue (stores indices)
        result = []

        for i in range(len(nums)):
            # Remove out-of-window indices from the front
            if mono_q and mono_q[0] == i - k:
                mono_q.popleft()

            # Remove smaller values from the back to maintain decreasing order
            while mono_q and nums[mono_q[-1]] < nums[i]:
                mono_q.pop()

            # Add current element's index
            mono_q.append(i)

            # Append the maximum for the current window
            if i >= k - 1:
                result.append(nums[mono_q[0]])
        return result