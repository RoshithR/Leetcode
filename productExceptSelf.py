# Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].
#
# The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.
#
# You must write an algorithm that runs in O(n) time and without using the division operation.


# def productExceptSelf(nums):
#     # The length of the input array
#     length = len(nums)
#
#     # The left and right arrays as described in the algorithm
#     L, R, answer = [0] * length, [0] * length, [0] * length
#
#     # L[i] contains the product of all the elements to the left
#     # Note: for the element at index '0', there are no elements to the left,
#     # so the L[0] would be 1
#     L[0] = 1
#     for i in range(1, length):
#         # L[i - 1] already contains the product of elements to the left of 'i - 1'
#         # Simply multiplying it with nums[i - 1] would give the product of all
#         # elements to the left of index 'i'
#         L[i] = nums[i - 1] * L[i - 1]
#
#     # R[i] contains the product of all the elements to the right
#     # Note: for the element at index 'length - 1', there are no elements to the right,
#     # so the R[length - 1] would be 1
#     R[length - 1] = 1
#     for i in reversed(range(length - 1)):
#         # R[i + 1] already contains the product of elements to the right of 'i + 1'
#         # Simply multiplying it with nums[i + 1] would give the product of all
#         # elements to the right of index 'i'
#         R[i] = nums[i + 1] * R[i + 1]
#
#     # Constructing the answer array
#     for i in range(length):
#         # For the first element, R[i] would be product except self
#         # For the last element of the array, product except self would be L[i]
#         # Else, multiple product of all elements to the left and to the right
#         answer[i] = L[i] * R[i]
#
#     return answer

def productExceptSelf(nums):
    # n = len(nums)
    # l, r, answer = [0]*n, [0]*n, [0]*n
    # l[0], r[n-1] = 1,1
    # for i in range(1,n):
    #     l[i] = l[i-1]*nums[i-1]
    # for i in range(n-2,-1,-1):
    #     r[i] = r[i+1]*nums[i+1]
    # print(l)
    # print(r)
    # for index,x in enumerate(zip(l,r)):
    #     answer[index] = x[0]*x[1]
    # return answer
    n = len(nums)
    l,r,answer = [0]*n, [0]*n, [0]*n
    l[0], r[n-1]= 1,1
    for i in range(1,n):
        l[i] = l[i-1]*nums[i-1]

    for i in reversed(range(n-1)):
        r[i] = r[i+1]*nums[i+1]
    for i in range(n):
        answer[i] = l[i]*r[i]
    return answer


nums = [1,2,3,4]
print(productExceptSelf(nums))