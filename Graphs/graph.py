class Graph:
    def __init__(self, num_vertices):
        self.graph = {}


    def add_edge(self, u, v):
        if u in self.graph:
            self.graph[u].add(v)
        else:
            self.graph[u] = {v}
        if v in self.graph:
            self.graph[v].add(u)
        else:
            self.graph[v] = {u}

    
    def adjacent_nodes(self, node):
        return list(self.graph[node])
    
