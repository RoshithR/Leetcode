#Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it can trap after raining.

def TrapRainWater(height):
    left_wall, right_wall = 0,0
    water=0
    left,right = 0, len(height)-1
    while left<right:
        if height[left]<height[right]:
            if height[left]>left_wall:
                left_wall = height[left]
            else:
                water+=left_wall-height[left]
            left+=1
        else:
            if height[right]>right_wall:
                right_wall = height[right]
            else:
                water+=right_wall-height[right]
            right-=1

    return water



height = [0,1,0,2,1,0,1,3,2,1,2,1]
print(TrapRainWater(height))