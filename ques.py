"""
N = 6
arr[] = {1,2,3,4,5,6}
Output: 6 1 5 2 4 3
Explanation: Max element = 6, min = 1, 
second max = 5, second min = 2, and 
so on... Modified array is : 6 1 5 2 4 3.
"""

def rearrange(n, nums):
    res = []
    i, j = 0, len(nums) - 1

    while i <= j:
        if i == j:
            res.append(nums[i])
        else:
            res.append(nums[j])
            res.append(nums[i])
        i += 1
        j -= 1
    return res



n = 6
arr = [1, 2, 3, 4, 5, 6]
print(rearrange(n, arr))
