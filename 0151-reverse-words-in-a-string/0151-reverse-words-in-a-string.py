class Solution:
    def reverseWords(self, s: str) -> str:
        def trim_spaces(s):
            # Remove leading/trailing spaces and reduce multiple spaces
            n = len(s)
            left, right = 0, n - 1
            while left <= right and s[left] == ' ':
                left += 1
            while left <= right and s[right] == ' ':
                right -= 1

            output = []
            while left <= right:
                if s[left] != ' ':
                    output.append(s[left])
                elif output and output[-1] != ' ':
                    output.append(' ')
                left += 1
            return output

        def reverse(l, left, right):
            while left < right:
                l[left], l[right] = l[right], l[left]
                left += 1
                right -= 1

        # 1. Trim spaces
        l = trim_spaces(s)

        # 2. Reverse entire string
        reverse(l, 0, len(l) - 1)

        # 3. Reverse each word
        n = len(l)
        start = 0
        for end in range(n):
            if end == n - 1 or l[end] == ' ':
                reverse(l, start, end if l[end] != ' ' else end - 1)
                start = end + 1

        return ''.join(l)