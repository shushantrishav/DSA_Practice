class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj = [[] for _ in range(numCourses)]
        for dest, src in prerequisites:
            adj[src].append(dest)

        visited = [0] * numCourses

        def dfs(course):
            if visited[course] == 1:
                return False  # cycle detected
            if visited[course] == 2:
                return True   # already processed

            visited[course] = 1  # mark as visiting

            for neighbor in adj[course]:
                if not dfs(neighbor):
                    return False

            visited[course] = 2  # mark as done
            return True

        for course in range(numCourses):
            if not dfs(course):
                return False

        return True