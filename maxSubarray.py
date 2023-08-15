def maxSubArray(nums):
    """
    :type nums: List[int]
    :rtype: int
    """

    newNums = nums.sort()
    return newNums

nums = [-1,-2,-2,-2,3,2,-2,0]
nums.sort()
print(nums)    
# print(maxSubArray(nums))
