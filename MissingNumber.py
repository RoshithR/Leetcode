# Given an array nums containing n distinct numbers in the range [0, n], return the only number in the range that is missing from the array.
#
# Follow up: Could you implement a solution using only O(1) extra space complexity and O(n) runtime complexity?

#Solution using hashset time complexity O(n)

# def missingNumber(nums):
#     num_set = set(nums)
#     n = len(nums)+1
#     for i in range(n):
#         if i not in num_set:
#             return i

#Solution using Gaussian formula, time complexity O(n). Gauss formula: sum= n(n+1)/2

def missingNumber(nums):
    expected_sum = len(nums)*(len(nums)+1)//2
    actual_sum = sum(nums)
    return expected_sum-actual_sum


nums = [3, 0, 1]
print(missingNumber(nums))