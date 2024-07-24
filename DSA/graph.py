class Graph:
    def __init__(self, edges):
        self.edges = edges
        self.graph_dict = {}
        for start, end in edges:
            if start in self.graph_dict:
                self.graph_dict[start].append(end)
            else:
                self.graph_dict[start] = [end]
        print(self.graph_dict)

    def find_paths(self, start, end, path=[]):
        path = path + [start]
        if start == end:
            return [path]
        if start not in self.graph_dict:
            return []
        paths = []
        for node in self.graph_dict[start]:
            if node not in path:
                new_path = self.find_paths(node, end, path) #different paths for node not in path
                for p in new_path:
                    paths.append(p)
        return paths

    def shortest_path(self,start,end,path=[]):
        path = path + [start]
        if start == end:
            return [path]
        if start not in self.graph_dict:
            return []
        for node in self.graph_dict[start]:
            if node not in path:
                sp = self.shortest_path(node, end, path)
                shortest_path = None
                if sp:
                    if shortest_path is None or len(sp) < len(shortest_path):
                        shortest_path = sp
        return shortest_path






if __name__ == '__main__':
    routes = [
        ("Mumbai", "Paris"),
        ("Mumbai", "Dubai"),
        ("Paris", "Dubai"),
        ("Paris", "New York"),
        ("Dubai", "New York"),
        ("New York", "Toronto"),
    ]
    routes_graph = Graph(routes)
    routes_graph.graph_dict
    print(routes_graph.find_paths('Paris', 'New York',[]))
    print(routes_graph.shortest_path('Paris', 'New York',[]))