#Given an array of integers numbers that is already sorted in ascending order, find two numbers such that they add up to a specific target number.
#Return the indices of the two numbers (1-indexed) as an integer array answer of size 2, where 1 <= answer[0] < answer[1] <= numbers.length.
#You may assume that each input would have exactly one solution and you may not use the same element twice.

def two_sumII(nums, target):
    low, high = 0, len(nums)-1
    while low<high:
        sum = nums[low] + nums[high]
        if sum==target:
            return [low,high]
        elif sum<target:
            low+=1
        else:
            high-=1
    return [-1,-1]


nums = [1,2,3,4,5,6,7]
print(two_sumII(nums,12))