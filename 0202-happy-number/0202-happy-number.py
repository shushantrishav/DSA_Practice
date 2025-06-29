class Solution:
    def isHappy(self, n: int) -> bool:
        def get_next(x):
            return sum(int(c) ** 2 for c in str(x))

        slow = n
        fast = get_next(n)

        while fast != 1 and slow != fast:
            slow = get_next(slow)
            fast = get_next(get_next(fast))

        return fast == 1