
def subsett(nums):
    result = []  
    subset = []  

   
    def dfs(i):
        if len(subset) >= 1:
            subsetCpy = subset.copy()
            subsetCpy.sort()
            result.append(subsetCpy)
        if i >= len(nums):
            return 

        subset.append(nums[i])
        dfs(i + 1)
        subset.pop()
        dfs(i + 1)
    dfs(0)
    
    return result
nums = [3,4,5,2]
value = subsett(nums)
value = [[], *value]

newArr = []
for ind in value:
    if(ind not in newArr):
        newArr.append(ind)
        
print(newArr)