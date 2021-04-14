#Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
#You may assume that each input would have exactly one solution, and you may not use the same element twice.
#You can return the answer in any order.

def two_sum(nums, target):
    num_dict = {}
    for index, num in enumerate(nums):
        balance = target-num
        if balance in num_dict:
            return [num_dict[balance], index]
        num_dict[num] = index

nums = [2,7,9,6,4]
target=11
print(two_sum(nums, target))