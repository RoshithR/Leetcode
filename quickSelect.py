# Given an integer array nums and an integer k, return the kth largest element in the array.
# Note that it is the kth largest element in the sorted order, not the kth distinct element.

# The most naive solution is to sort the array and then send the kth element, that is O(nlogn) solution.
#This can be improved to O(nlogk) by using heap/priority queue
# import heapq
# def kthlargestElement(nums, k):
#     return heapq.nlargest(k,nums)[-1]
#
# nums = [3, 2, 1, 5, 6, 4]
# k = 2
# print(kthlargestElement(nums,k))

def partition(nums, low, high):
    pivot_index = (low+high)//2
    nums[pivot_index], nums[high] = nums[high], nums[pivot_index]
    store_index = low
    for i in range(low, high):
        if nums[i]<nums[high]:
            nums[i], nums[store_index] = nums[store_index], nums[i]
            store_index+=1
    nums[store_index], nums[high] = nums[high], nums[store_index]
    return store_index

def select(nums, low, high, ksmallest):
    if low==high:
        return nums[low]
    pivot = partition(nums, low, high)
    if ksmallest == pivot:
        return nums[ksmallest]
    elif ksmallest < pivot:
        return select(nums, low, pivot-1, ksmallest)
    else:
        return select(nums, pivot+1,high, ksmallest)
#
# def findKthLargest(nums, k):
#     """
#     :type nums: List[int]
#     :type k: int
#     :rtype: int
#     """
#
#     def partition(left, right, pivot_index):
#         pivot = nums[pivot_index]
#         # 1. move pivot to end
#         nums[pivot_index], nums[right] = nums[right], nums[pivot_index]
#
#         # 2. move all smaller elements to the left
#         store_index = left
#         for i in range(left, right):
#             if nums[i] < pivot:
#                 nums[store_index], nums[i] = nums[i], nums[store_index]
#                 store_index += 1
#
#         # 3. move pivot to its final place
#         nums[right], nums[store_index] = nums[store_index], nums[right]
#
#         return store_index
#
#     def select(left, right, k_smallest):
#         """
#         Returns the k-th smallest element of list within left..right
#         """
#         if left == right:  # If the list contains only one element,
#             return nums[left]  # return that element
#
#         # select a random pivot_index between
#         # pivot_index = random.randint(left, right)
#         pivot_index = (left+right)//2
#
#         # find the pivot position in a sorted list
#         pivot_index = partition(left, right, pivot_index)
#
#         # the pivot is in its final sorted position
#         if k_smallest == pivot_index:
#             return nums[k_smallest]
#         # go left
#         elif k_smallest < pivot_index:
#             return select(left, pivot_index - 1, k_smallest)
#         # go right
#         else:
#             return select(pivot_index + 1, right, k_smallest)
#
#     # kth largest is (n - k)th smallest
#     return select(0, len(nums) - 1, len(nums) - k)

nums = [3, 2, 1, 5, 6, 4]
k = 2
nk = len(nums)-k
print(select(nums, 0, len(nums)-1, nk))
# print(findKthLargest(nums,k))