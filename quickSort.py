
def maxSubArray(nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if (len(nums) == 1):
            return nums[0]

        def quickSort(nums, sums=[]):
            if (len(nums) >= 1):
                currentSum = sum(nums)
                sums.append(currentSum)

            if len(nums) <= 1:
                return 1
            else:
                pivot = nums.index(min(nums))
                if nums[pivot] < 0:
                    quickSort(nums[:pivot], sums)
                    quickSort(nums[pivot + 1:], sums)
            return sums

        sums = quickSort(nums)
        greatestSum = max(sums)
        return greatestSum