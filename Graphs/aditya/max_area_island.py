# aproach is 1. check if grid has 1 or not.
# 

def maxAreaOfIsland(grid):
    if not grid:
        return 0

    
    def dfs(grid, i, j, count):
        if i<0 or j<0 or i>=len(grid) or j>=len(grid[0]) or grid[i][j] == 0:
            return 0

        count=1
        grid[i][j] = 0
        # check all four sides
        count+=dfs(grid, i,j+1, count)
        count+=dfs(grid, i, j-1, count)
        count+=dfs(grid, i+1, j, count)
        count+=dfs(grid, i-1, j, count)
        
        return count

    answer = 0
    count = 0
    
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == 1:
                answer = max(answer, (dfs(grid, i,j,count)))
                


    return answer

grid = [[0,0,1,0,0,0,0,1,0,0,0,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,1,1,0,1,0,0,0,0,0,0,0,0],[0,1,0,0,1,1,0,0,1,0,1,0,0],[0,1,0,0,1,1,0,0,1,1,1,0,0],[0,0,0,0,0,0,0,0,0,0,1,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,0,0,0,0,0,0,1,1,0,0,0,0]]
print(maxAreaOfIsland(grid))