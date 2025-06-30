class Solution:
    def maxNumOfSubstrings(self, s: str) -> List[str]:
        n = len(s)
        first = {}
        last = {}

        # Step 1: Record first and last occurrence for each character
        for i, c in enumerate(s):
            if c not in first:
                first[c] = i
            last[c] = i

        intervals = []

        # Step 2: Try to expand intervals for each character
        for c in set(s):
            l = first[c]
            r = last[c]
            j = l
            while j <= r:
                if first[s[j]] < l:
                    l = first[s[j]]
                    j = l
                if last[s[j]] > r:
                    r = last[s[j]]
                j += 1
            if l == first[c]:  # Only add if it's valid
                intervals.append((l, r))

        # Step 3: Greedily select non-overlapping substrings
        intervals.sort(key=lambda x: x[1])  # sort by end position
        res = []
        end = -1

        for l, r in intervals:
            if l > end:
                res.append(s[l:r+1])
                end = r

        return res