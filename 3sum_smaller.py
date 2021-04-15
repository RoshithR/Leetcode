#Given an array of n integers nums and an integer target
# , find the number of index triplets i, j, k with 0 <= i < j < k < n that satisfy the condition nums[i] + nums[j] + nums[k] < target.

def threeSumSmaller(nums,target):
    nums.sort()
    ans=0
    for i in range(len(nums)-2):
        lo, hi = i+1,len(nums)-1
        while lo<hi:
            sum = nums[i]+nums[lo]+nums[hi]
            if sum<target:
                ans+=hi-lo
                lo+=1
            else:
                hi-=1
    return ans

# ts = threeSum_smaller()
nums=[-2,0,1,3]
target=2
print(threeSumSmaller(nums,target))