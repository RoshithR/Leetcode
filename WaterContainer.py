# Given n non-negative integers a1, a2, ..., an , where each represents a point at coordinate (i, ai).
# n vertical lines are drawn such that the two endpoints of the line i is at (i, ai) and (i, 0).
# Find two lines, which, together with the x-axis forms a container, such that the container contains the most water.

def largest_area(height):
    #BRUTE FORCE O(n^2)
    # res,area=0,0
    # for l in range(len(height)):
    #     for r in range(l+1,len(height)):
    #         area = (r-l)*min(height[l],height[r])
    #         res = max(res,area)
    # return res
    l,r = 0,len(height)-1
    res,area=0,0
    while l<r:
        area = (r-l)*min(height[r],height[l])
        res = max(res, area)
        if height[r]<height[l]:
            r-=1
        else:
            l+=1
    return res

height = [1,8,6,2,5,4,8,3,7]
print(largest_area(height))