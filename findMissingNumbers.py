#Given a sorted array find the missing numbers

#O(M^2) approach

# def findMissingElements(arr,N):
#     diff = arr[0]
#     res= []
#     for i in range(N):
#         if arr[i] - i != diff:
#             while diff<arr[i]-i:
#                 res.append(diff+i)
#                 diff+=1
#     return res
#
#
# # Driver Code
#
# # Given array arr[]
# arr = [6, 7, 10, 11, 13]
#
# N = len(arr)
#
# # Function call
# print(findMissingElements(arr,N))

#O(M) approach where M is the largest element in the array

# Function to find the missing elements
# def printMissingElements(arr, N):
#     # Initialize an array with zero
#     # of size equals to the maximum
#     # element in the array
#     b = [0] * (arr[N - 1] + 1)
#
#     # Make b[i]=1 if i is present
#     # in the array
#     for i in range(N):
#         # If the element is present
#         # make b[arr[i]]=1
#         b[arr[i]] = 1
#
#     # Print the indices where b[i]=0
#     for i in range(arr[0], arr[N - 1] + 1):
#         if (b[i] == 0):
#             print(i, end=" ")

def printMissingElements(arr,N):
    b = [0]*(arr[N-1]+1)
    for i in range(N):
        b[arr[i]]=1
    for i in range(arr[0],arr[N-1]+1):
        if b[i]==0:
            print(i)

# Driver Code

# Given array arr[]
arr = [6, 7, 10, 11, 13]

N = len(arr)

# Function call
printMissingElements(arr, N)