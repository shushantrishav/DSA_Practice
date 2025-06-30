class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj = [[] for _ in range(numCourses)]
        in_degree = [0] * numCourses

        for dest, src in prerequisites:
            adj[src].append(dest)
            in_degree[dest] += 1

        queue = deque([i for i in range(numCourses) if in_degree[i] == 0])
        count = 0

        while queue:
            course = queue.popleft()
            count += 1

            for neighbor in adj[course]:
                in_degree[neighbor] -= 1
                if in_degree[neighbor] == 0:
                    queue.append(neighbor)

        return count == numCourses