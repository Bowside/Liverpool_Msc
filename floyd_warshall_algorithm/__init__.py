from pathlib import Path
import os

INF = float('INF')

def floyd_warshall_recursive(graph, n):
    def helper(dist, k, i, j):
        if k == 0:
            return dist[i][j]
        else:
            return min(helper(dist, k-1, i, j), helper(dist, k-1, i, k) + helper(dist, k-1, k, j))

    dist = [[INF] * n for _ in range(n)]

    for i in range(n):
        for j in range(n):
            dist[i][j] = graph[i][j]

    for k in range(n):
        for i in range(n):
            for j in range(n):
                dist[i][j] = helper(dist, k, i, j)

    return dist

def read_graph(filename):
    with open(filename, 'r') as file:
        lines = file.readlines()
        n, _ = map(int, lines[0].split())
        graph = [[INF] * n for _ in range(n)]
        for line in lines[1:]:
            u, v, weight = map(int, line.split())
            graph[u][v] = weight
        return graph, n


if __name__ == '__main__':
    try:
        relative_path = os.path.dirname(__file__)
        user_input = Path(relative_path, input("Enter the relative path of your file: "))
        if not user_input.exists():
            raise ValueError(f"I did not find the file at {user_input}")
        graph, num_vertices = read_graph(user_input)
        result = floyd_warshall_recursive(graph, num_vertices)
        print(result)
    except Exception as e: 
        print(e)