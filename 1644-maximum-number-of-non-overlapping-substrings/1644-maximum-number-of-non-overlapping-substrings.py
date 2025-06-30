class Solution:
    def maxNumOfSubstrings(self, s: str) -> List[str]:
        n = len(s)
        mins = [float('inf')] * 26
        maxs = [-1] * 26
        exists = [False] * 26

        # Pre-compute mins and maxs
        for i, c in enumerate(s):
            idx = ord(c) - ord('a')
            mins[idx] = min(mins[idx], i)
            maxs[idx] = max(maxs[idx], i)
            exists[idx] = True

        # Pre-compute prefix sums
        prefix_sum = [[0] * 26 for _ in range(n + 1)]
        for i in range(n):
            for j in range(26):
                prefix_sum[i + 1][j] = prefix_sum[i][j]
            prefix_sum[i + 1][ord(s[i]) - ord('a')] += 1

        # Build adjacency matrix graph
        graph = [[False] * 26 for _ in range(26)]
        for i in range(26):
            if exists[i]:
                for j in range(26):
                    if prefix_sum[maxs[i] + 1][j] - prefix_sum[mins[i]][j] > 0:
                        graph[i][j] = True

        # First DFS to compute finishing times (postorder)
        stack = []
        visited = [False] * 26

        def dfs1(v):
            visited[v] = True
            for u in range(26):
                if graph[v][u] and not visited[u]:
                    dfs1(u)
            stack.append(v)

        for i in range(26):
            if exists[i] and not visited[i]:
                dfs1(i)

        # Second DFS on transposed graph to assign SCC batches
        batches = [-1] * 26
        degree = [0] * 26  # Out-degree for each SCC batch
        batch = 0

        def dfs2(v, batch):
            batches[v] = batch
            for u in range(26):
                if graph[u][v]:
                    if batches[u] == -1:
                        dfs2(u, batch)
                    elif batches[u] != batch:
                        degree[batches[u]] += 1

        while stack:
            v = stack.pop()
            if batches[v] == -1:
                dfs2(v, batch)
                batch += 1

        # Collect valid substrings from SCCs with zero out-degree
        result = []
        for b in reversed(range(batch)):
            if degree[b] == 0:
                l, r = float('inf'), -1
                for i in range(26):
                    if batches[i] == b:
                        l = min(l, mins[i])
                        r = max(r, maxs[i])
                result.append(s[l:r+1])

        return result