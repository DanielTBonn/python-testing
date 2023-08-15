def maxSubArray(nums):
    """
    :type nums: List[int]
    :rtype: int
    """

    pointer1 = front_index = 0
    pointer2 = back_index = length = len(nums)
    greatestSum = sum(nums)

    if length <= 1:
        return greatestSum

    while pointer1 < length:
        
        checkSum = sum(nums[pointer1:length])
        if checkSum > greatestSum and len(nums[pointer1:length]) > 0:
            greatestSum = checkSum
            front_index = pointer1

        pointer1 += 1

    greatestSum = sum(nums)
    while pointer2 > 0:
        
        checkSum = sum(nums[0:pointer2])
        if checkSum > greatestSum and len(nums[0:pointer2]) > 0:
            greatestSum = checkSum
            back_index = pointer2

        pointer2 -= 1

    frontSum = sum(nums[front_index:length])
    backSum = sum(nums[0:back_index])
    if len(nums[front_index:back_index]) > 0:
        greatestSum = sum(nums[front_index:back_index])
    else:
        greatestSum = frontSum

    if (frontSum > greatestSum):
        greatestSum = frontSum

    if (backSum > greatestSum):
        greatestSum = backSum

    if (max(nums) > greatestSum):
        return max(nums)
    else:
        return greatestSum

nums = [-1,-2,-2,-2,3,2,-2,0]
print(maxSubArray(nums))    
