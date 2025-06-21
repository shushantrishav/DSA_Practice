class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        import math
    
        numbers = [str(i) for i in range(1, n+1)]
        result = []
        k -= 1  # convert to 0-based index
    
        while n > 0:
            fact = math.factorial(n-1)
            index = k // fact
            result.append(numbers[index])
            numbers.pop(index)
        
            k = k % fact
            n -= 1
    
        return ''.join(result)