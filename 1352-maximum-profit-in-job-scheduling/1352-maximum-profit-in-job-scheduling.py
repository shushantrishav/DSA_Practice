class Solution:
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        # Combine and sort jobs by end time
        jobs = sorted(zip(startTime, endTime, profit), key=lambda x: x[1])
        n = len(jobs)
        
        # dp: list of (end_time, max_profit up to this time)
        dp = [(0, 0)]  # Base case: (time 0, profit 0)

        for s, e, p in jobs:
            # Find latest dp where end_time <= start time of current job
            i = bisect.bisect_right(dp, (s, float('inf'))) - 1
            current_profit = dp[i][1] + p

            # Only update if it's better than last recorded profit
            if current_profit > dp[-1][1]:
                dp.append((e, current_profit))

        return dp[-1][1]