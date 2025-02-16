from collections import deque

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
        
        
    def bfs(self, start):
        visted = set()
        q = deque([start])
        visted.add(start)
        
        while q:
            node = q.popleft()
            print(node, end=" ")
            
            for neighbour in self.graph[node]:
                if neighbour not in visted:
                    visted.add(neighbour)
                    q.append(neighbour)
                    
        
            
            
g = Graph()

g.add(1,2)
g.add(1,3)
g.add(1,4)
g.add(2,5)

g.bfs(1)
