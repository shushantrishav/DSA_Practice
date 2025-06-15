class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        result = []
        
        for rows in range(numRows):
            ans = 1
            ansRow = [1]
            for col in range(1,rows+1):
                ans = (ans * (rows - col+1)) // col
                ansRow.append(ans)
            result.append(ansRow)

        return result