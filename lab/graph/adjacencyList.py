from collections import deque


class Graph:
    def __init__(self):
        self.adjacency_list = {}

    def add_vertex(self, node):
        if node not in self.adjacency_list:
            self.adjacency_list[node] = []

    def add_edge(self, vertex_a, vertex_b, bidirectional=True):
        self.add_vertex(vertex_a)
        self.add_vertex(vertex_b)
        self.adjacency_list[vertex_a].append(vertex_b)
        if bidirectional:
            self.adjacency_list[vertex_b].append(vertex_a)

    def __str__(self):
        return '\n'.join(f'{k}: {v}' for k, v in self.adjacency_list.items())


def dfs(graph: Graph, vertex_start, vertex_visited=None):
    if vertex_visited is None:
        vertex_visited = set()
    vertex_visited.add(vertex_start)
    print(vertex_start, end='')
    for v in graph.adjacency_list[vertex_start]:
        if v not in vertex_visited:
            dfs(graph, v, vertex_visited)


def bfs(graph: Graph, vertex_start):
    vertex_visited = set()
    queue = deque([vertex_start])
    vertex_visited.add(vertex_start)
    while queue:
        vertex = queue.popleft()
        print(vertex, end='')
        for i in graph.adjacency_list[vertex]:
            if i not in vertex_visited:
                vertex_visited.add(i)
                queue.append(i)


if __name__ == '__main__':
    g = Graph()
    g.add_edge('A', 'B')
    g.add_edge('A', 'C')
    g.add_edge('B', 'D')
    print(g, end='\n\n')
    dfs(g, 'A')
    print(end='\n\n')
    bfs(g, 'A')
