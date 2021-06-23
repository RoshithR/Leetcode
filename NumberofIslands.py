# Given an m x n 2D binary grid grid which represents a map of '1's (land) and '0's (water), return the number of islands.
# An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically.
# You may assume all four edges of the grid are all surrounded by water.



def numIslands(grid):
    count=0
    if not grid:
        return count
    x_max,y_max = len(grid), len(grid[0])

    def helper(x,y):
        if 0<=x<x_max and 0<=y<y_max and grid[x][y]=="1":
            grid[x][y]="0"
            helper(x+1,y)
            helper(x-1,y)
            helper(x,y+1)
            helper(x,y-1)
    for x_idx in range(x_max):
        for y_idx in range(y_max):
            if grid[x_idx][y_idx]=="1":
                count+=1
                helper(x_idx,y_idx)
    return count


# Input: grid = [
#   ["1","1","1","1","0"],
#   ["1","1","0","1","0"],
#   ["1","1","0","0","0"],
#   ["0","0","0","0","0"]
# ]
# Output: 1

grid = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]

print(numIslands(grid))