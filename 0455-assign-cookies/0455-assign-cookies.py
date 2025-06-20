class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()

        ptrChild = 0  # pointer for g (children)
        ptrCookies = 0  # pointer for s (cookies)
        n = len(g)
        m = len(s)

        content_children = 0

        while ptrChild < n and ptrCookies < m:
            if s[ptrCookies] >= g[ptrChild]:
                content_children += 1
                ptrChild += 1
            ptrCookies += 1

        return content_children