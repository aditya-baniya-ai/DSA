# I will approach this problem by checking all the nodes in graph
# if it is 1 then we run a recursive dfs on this and make 0 for every 1 if they are connected to each other
# that means that is one land connected together

def number_of_islands(grid):
    if not grid:
        return 0
    
    def dfs(grid, i ,j):
        if i<0 or j<0 or i<len(grid) or j<len(grid[0]) or grid[i][j]=="0":
            return
        
        # checking all the four sides if they have 1
        dfs(i,j+1)
        dfs(i,j-1)
        dfs(i+1,j)
        dfs(i-1,j)
        
    count = 0
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == "1":
                count+=1
                dfs(grid, i,j)
                
    return count
            