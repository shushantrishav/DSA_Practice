class Solution:
    def reverseWords(self, s: str) -> str:
        # Split by whitespace, ignoring multiple spaces, and reverse the list
        words = s.split()
        # Join with a single space
        return ' '.join(words[::-1])