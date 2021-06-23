
# Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.

def maxSubArray(nums):
    max_subarray = curr_subarray = 0
    for num in nums:
        curr_subarray=max(num, curr_subarray+num)
        max_subarray = max(max_subarray, curr_subarray)
    return max_subarray

nums = [-2,1,-3,4,-1,2,1,-5,4]
print(maxSubArray(nums))