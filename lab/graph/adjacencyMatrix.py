from collections import deque


class Graph:
    def __init__(self, size):
        self.size = size
        self.adjacency_matrix = [[0] * size for _ in range(size)]

    def add_edge(self, idx_a, idx_b, bidirectional=True):
        self.adjacency_matrix[idx_a][idx_b] = 1
        if bidirectional:
            self.adjacency_matrix[idx_b][idx_a] = 1

    def display(self):
        for row in self.adjacency_matrix:
            print(row)


def dfs(graph: Graph, idx_start: int, indexes_visited=None):
    if indexes_visited is None:
        indexes_visited = [False] * graph.size
    print(idx_start, end='')
    indexes_visited[idx_start] = True
    for i in range(graph.size):
        if graph.adjacency_matrix[idx_start][i] != 0 and not indexes_visited[i]:
            dfs(graph, i, indexes_visited)


def bfs(graph, idx_start):
    indexes_visited = [False] * graph.size
    queue = deque([idx_start])
    indexes_visited[idx_start] = True
    while queue:
        idx_vertex = queue.popleft()
        print(idx_vertex, end='')
        for idx in range(graph.size):
            if graph.adjacency_matrix[idx_vertex][idx] != 0 and not indexes_visited[idx]:
                indexes_visited[idx] = True
                queue.append(idx)


if __name__ == '__main__':
    g = Graph(5)
    g.add_edge(0, 1)
    g.add_edge(0, 2)
    g.add_edge(1, 3)
    g.add_edge(2, 4)
    g.display()
    print(end='\n\n')
    dfs(g, 0)
    print(end='\n')
    bfs(g, 0)
