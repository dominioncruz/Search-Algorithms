#Backtracking builds candidates to a solution and eliminates ones that can't be solutions.
def subset_sum(arr, i, sum):
    k = len(arr) -1
    if(sum == 0):
        return True
    if(sum < 0):
        return False
    if(i > k) and (sum != 0):
        return False
    left = subset_sum(arr, i + 1, sum- arr[i])
    right = subset_sum(arr, i + 1, sum) 
    return left or right

arr = [3,4,5,2]
sum = 14
track = False
print(subset_sum(arr,0, sum))

    