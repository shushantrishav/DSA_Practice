class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []
    
        def backtrack(idx, current, total):
            if total == target:
                result.append(current[:])
                return
            if total > target or idx == len(candidates):
                return
        
            # Pick the current number (unlimited times)
            current.append(candidates[idx])
            backtrack(idx, current, total + candidates[idx])
        
            # Don't pick the current number
            current.pop()
            backtrack(idx + 1, current, total)
    
        backtrack(0, [], 0)
        return result