# Given an integer array nums and an integer k, return the k most frequent elements. You may return the answer in any order.

from collections import Counter
import random


# def topKFrequent(nums, k):
#     count = Counter(nums)
#     unique = list(count.keys())
#
#     def partition(left, right, pivot_index):
#         pivot_frequency = count[unique[pivot_index]]
#         # 1. move pivot to end
#         unique[pivot_index], unique[right] = unique[right], unique[pivot_index]
#
#         # 2. move all less frequent elements to the left
#         store_index = left
#         for i in range(left, right):
#             if count[unique[i]] < pivot_frequency:
#                 unique[store_index], unique[i] = unique[i], unique[store_index]
#                 store_index += 1
#
#         # 3. move pivot to its final place
#         unique[right], unique[store_index] = unique[store_index], unique[right]
#
#         return store_index
#
#     def quickselect(left, right, k_smallest):
#         """
#         Sort a list within left..right till kth less frequent element
#         takes its place.
#         """
#         # base case: the list contains only one element
#         if left == right:
#             return
#
#         # select a random pivot_index
#         pivot_index = random.randint(left, right)
#
#         # find the pivot position in a sorted list
#         pivot_index = partition(left, right, pivot_index)
#
#         # if the pivot is in its final sorted position
#         if k_smallest == pivot_index:
#             return
#             # go left
#
#         elif k_smallest < pivot_index:
#             quickselect(left, pivot_index - 1, k_smallest)
#         # go right
#         else:
#             quickselect(pivot_index + 1, right, k_smallest)
#
#     n = len(unique)
#     # kth top frequent element is (n - k)th less frequent.
#     # Do a partial sort: from less frequent to the most frequent, till
#     # (n - k)th less frequent element takes its place (n - k) in a sorted array.
#     # All element on the left are less frequent.
#     # All the elements on the right are more frequent.
#     quickselect(0, n - 1, n - k)
#     # Return top k frequent elements
#     return unique[n - k:]

def topKFrequent(nums,k):
    count = Counter(nums)
    unique = list(count.keys())
    def partition(low, high):
        pivot_index = (low+high)//2
        pivot_frequency = count[pivot_index]
        unique[pivot_index], unique[high] = unique[high], unique[pivot_index]
        indx = low
        for i in range(low, high):
            if count[unique[i]]<pivot_frequency:
                unique[i], unique[low] = unique[low], unique[i]
                indx+=1
        unique[indx], unique[high] = unique[high], unique[indx]
        return indx

    def select(low, high, ksmallest):
        if low==high:
            return
        pivot = partition(low,high)
        if ksmallest == pivot:
            return
        elif ksmallest<pivot:
            select(low, pivot-1, ksmallest)
        else:
            select(pivot+1,low,ksmallest)

    n = len(unique)
    select(0, n-1, n-k)
    return unique[n-k:]




nums = [1,1,1,2,2,3]
k = 2
print(topKFrequent(nums,k))