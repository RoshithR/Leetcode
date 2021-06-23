# Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.


#Two pointer method
class threeSum_twopointer:
    def threeSum(self, nums):
        res=[]
        nums.sort()
        for i in range(len(nums)):
            if nums[i]>=0:
                break
            elif i==0 or nums[i]!=nums[i-1]:
                self.twoSum(nums,i,res)
        return res
    def twoSum(self, nums, i, res):
        lo, hi = i+1,len(nums)-1
        while lo<hi:
            sum = nums[i]+nums[lo]+nums[hi]
            if sum==0:
                res.append([nums[i],nums[lo],nums[hi]])
                lo+=1
                hi-=1
                while lo<hi and nums[lo]==nums[lo-1]:
                    lo+=1
            elif sum<0:
                lo+=1
            else:
                hi-=1

class threeSum_hashmap:
    def threeSum(self, nums):
        nums.sort()
        res=[]
        for i in range(len(nums)):
            if nums[i]>=0:
                break
            elif i==0 or nums[i]!=nums[i-1]:
                self.twoSum(nums,i,res)
        return res
    def twoSum(self, nums,i, res):
        seen = set()
        j=i+1
        while j<len(nums):
            target = -nums[i]-nums[j]
            if target in seen:
                res.append([nums[i],nums[j],target])
                while j+1<len(nums) and nums[j]==nums[j+1]:
                    j+=1
            seen.add(nums[j])
            j += 1

# class threeSum_withoutSort:
#     def threeSum(self, nums):
#         res, dups = set(), set()
#         seen = {}
#         for i, val1 in enumerate(nums):
#             if val1 not in dups:
#                 dups.add(val1)
#                 for j, val2 in enumerate(nums[i + 1:]):
#                     complement = -val1 - val2
#                     if complement in seen and seen[complement] == i:
#                         res.add(tuple(sorted((val1, val2, complement))))
#                     seen[val2] = i
#         return res

class threeSum_withoutSort:
    def threeSum(self, nums):
        res=set()
        for i, val1 in enumerate(nums):
            seen={}
            for j,val2 in enumerate(nums[i+1:]):
                complement = -val1-val2
                if complement in seen and seen[complement]==i:
                    res.add(tuple(sorted((val1,val2,complement))))
                seen[val2]=i
        return res



# ts=threeSum_hashmap()
ts = threeSum_withoutSort()
nums=[-1,0,1,2,-1,-4]
print(ts.threeSum(nums))


