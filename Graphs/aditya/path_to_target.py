class Graph:
    def __init__(self):
        self.graph = {}
        
        
    def add(self, u,v):
        if u not in self.graph:
            self.graph[u] = []
        if v not in self.graph:
            self.graph[v] = []
            
            
        self.graph[u].append(v)
        self.graph[v].append(u)
        
        
    def path(self, visited, string, curr, target):
        string+=str(curr) + "->"
        
        if curr==target:
            print(string)
            return
        
        visited.add(curr)
        
        for neighbour in self.graph[curr]:
            if neighbour not in visited:
                self.path(visited,string,neighbour, target)
                
        visited.remove(curr) # for backtracking
        
        
        
g = Graph()
g.add(0,1)
g.add(1,3)
g.add(3,5)
g.add(3,4)
g.add(5,6)
g.add(4,5)
g.add(2,4)
g.add(0,2)

visited = set()
g.path(visited, "", 0, 5)
