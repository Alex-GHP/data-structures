class Graph:
    def __init__(self):
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
    

    def unconnected_vertices(self):
        unconnected = []
        for key, values in self.graph.items():
            if not values:
                unconnected.append(key)
        return unconnected
    

    def edge_exists(self, u, v):
        if u in self.graph and v in self.graph:
            return (v in self.graph[u]) and (u in self.graph[v])
        return False
    
    
    def breadth_first_search(self, v):
        visited = []
        to_visit = [v]
        while to_visit:
            vertex = to_visit.pop(0)
            visited.append(vertex)

            for neighbor in sorted(self.graph[vertex]):
                if neighbor not in visited and neighbor not in to_visit:
                    to_visit.append(neighbor)

        return visited
    
