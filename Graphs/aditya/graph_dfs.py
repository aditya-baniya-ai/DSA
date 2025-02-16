class Graph:
    def __init__(self):
        self.graph = {}
        
    def add(self,u,v):
        if u not in self.graph:
            self.graph[u] = []
            
        if v not in self.graph:
            self.graph[v] = []
            
        self.graph[u].append(v)
        self.graph[v].append(u)
        
    def dfs(self, visited, curr):
        if curr in visited:
            return
        
        print(curr)
        visited.add(curr)
        
        for neighbour in self.graph[curr]:
            self.dfs(visited, neighbour)
        
        
g = Graph()
visited = set()

g.add(1,2)
g.add(1,3)
g.add(1,4)
g.add(2,5)

g.dfs(visited, 1)
        