def combinationSum(candidates, target):
    res = []
    
    def backtrack(start, curr, total):
        if total == target:
            res.append(list(curr))
            return
        if total > target:
            return
        
        for i in range(start, len(candidates)):
            curr.append(candidates[i])
            backtrack(i, curr, total + candidates[i])
            curr.pop()
    
    backtrack(0, [], 0)
    return res
