
def helper(nums, low, high):
    if low <= high:
        bestPivot = quicksort(nums, low, high)

        helper(nums, low, bestPivot -1)
        helper(nums, bestPivot +1, high)

def quicksort(nums, low, high):
    pivot, i = high, low - 1

    for j in range(low, high):

        if nums[j] <= nums[pivot]:
            i += 1
            nums[i], nums[j] = nums[j], nums[i]

    nums[ i +1], nums[high] = nums[high], nums[ i +1]

    return i+ 1


nums = [2, 8, 1, 3, 7, 6, 4, 5]
helper(nums, 0, len(nums) - 1)
print(nums)

'''
Idea: take a pivot point, last value of array
      try to bring it somewhere in middle where all values left to it
      are smaller than it and at right bigger than it
      repeat this for the rest of the left and right subarray individually

Execution:
    track 2 points, i at -1 and j from 0 to pivot-1
    if j is <= value at pivot, we increment i and swap i, j values

    this way we would end up having all value smaller than pivot
    on left side and all greater on right side of nums, 
    the pivot value is still at last as of now, so smth like 2 1 3 4 6 7 8 5*

    now we swap i+1 and pivot values once loop ends
    as i+1 is the correct index of pivot, smth like 2 1 3 4 5* 7 8 6
    
    we repeat this process for nums[:i+1] and nums[i+1:] until all pivots
    are at correct indices

Video: BroCode
'''