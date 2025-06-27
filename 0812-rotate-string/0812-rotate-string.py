class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        if len(s) != len(goal):
            return False

        def compute_z(string):
            n = len(string)
            z = [0] * n
            l, r = 0, 0

            for i in range(1, n):
                if i <= r:
                    z[i] = min(r - i + 1, z[i - l])

                while i + z[i] < n and string[z[i]] == string[i + z[i]]:
                    z[i] += 1

                if i + z[i] - 1 > r:
                    l, r = i, i + z[i] - 1

            return z

        concat = goal + "$" + s + s
        z = compute_z(concat)

        return any(val == len(goal) for val in z)
