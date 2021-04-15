# Given an array nums of n integers and an integer target, find three integers in nums such that the sum is closest to target.
# Return the sum of the three integers. You may assume that each input would have exactly one solution.

# def threeSum(nums,target):
#     nums.sort()
#     diff = float('inf')
#     for i in range(len(nums)-1):
#         lo,hi = i+1,len(nums)-1
#         while lo<hi:
#             sum=nums[i]+nums[lo]+nums[hi]
#             balance = target-sum
#             if balance ==0:
#                 return 0
#             elif abs(balance) < abs(diff):
#                 diff = balance
#                 if sum>target:
#                     hi-=1
#                 else:
#                     lo+=1
#     return diff
def threeSum(nums,target):
    nums.sort()
    diff = float('inf')
    for i in range(len(nums)):
        lo,hi = i+1,len(nums)-1
        while lo<hi:
            sum=nums[i]+nums[lo]+nums[hi]
            if abs(target-sum) < abs(diff):
                diff = target - sum
            if sum>target:
                hi-=1
            else:
                lo+=1
        if diff == 0:
            break
    return target - diff


nums = [-1,2,1,-4]
target = 1
print(threeSum(nums,target))
