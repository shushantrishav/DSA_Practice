class Solution:
    def repeatedStringMatch(self, a: str, b: str) -> int:
        repeated_a = a
        count = 1

        # Repeat a until its length is >= length of b
        while len(repeated_a) < len(b):
            repeated_a += a
            count += 1

        # Check if b is now a substring
        if b in repeated_a:
            return count

        # Check one more time after adding one more a (for overlap cases)
        repeated_a += a
        count += 1
        if b in repeated_a:
            return count

        # Otherwise impossible
        return -1