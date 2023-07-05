"""
A class that implements the Floyd-Warshall algorithm to find the shortest distances
between all pairs of vertices in a graph using a recursive approach.
"""
class FloydWarshallRecursive:
    """
    A class that implements the Floyd-Warshall algorithm to find the shortest distances 
    between all pairs of vertices in a graph using a recursive approach.
    """

    def calc_shortest_distance(self, graph: list, num_vertices: int):
        """
        Applies the Floyd-Warshall algorithm recursively to find the shortest distances 
        between all pairs of vertices in a graph.

        Args:
            graph (List[List[float]]): The adjacency matrix representation of the graph.
            num_vertices (int): The number of vertices in the graph.

        Returns:
            List[List[float]]: A 2D matrix representing the shortest distances between 
            all pairs of vertices.
        """

        def helper(dist, k, i, j):
            """
            Recursive helper function to calculate the shortest distance between two 
            vertices using intermediate vertices.

            Args:
                dist (List[List[float]]): The current matrix of shortest distances.
                k (int): The intermediate vertex index to consider.
                i (int): The index of the starting vertex.
                j (int): The index of the ending vertex.

            Returns:
                float: The shortest distance between the starting vertex and the ending 
                vertex.
            """
         
            if k == 0:
                return dist[i][j]
            else:
                return min(helper(dist, k-1, i, j), helper(dist, k-1, i, k) + helper(dist, k-1, k, j))

        dist = [[self.inf] * num_vertices for _ in range(num_vertices)]

        for i in range(num_vertices):
            for j in range(num_vertices):
                dist[i][j] = graph[i][j]

        for k in range(num_vertices):
            for i in range( num_vertices):
                for j in range(num_vertices):
                    dist[i][j] = helper(dist, k, i, j)

        return dist

    def read_graph(self, filename):
        """
        Reads a graph from a file and constructs its adjacency matrix representation.

        Args:
            filename (str): The path to the file containing the graph data.

        Returns:
            tuple: A tuple containing the adjacency matrix representation of the graph 
                   and the number of vertices. The adjacency matrix is represented as 
                   a 2D list, and the number of vertices is an integer.
        """
    
        with open(filename, 'r') as file:
            lines = file.readlines()
            n, _ = map(int, lines[0].split())
            graph = [[self.inf] * n for _ in range(n)]
            for line in lines[1:]:
                u, v, weight = map(int, line.split())
                graph[u][v] = weight
            return graph, n
 
    def __init__(self) -> None:
        """
        Initializes the FloydWarshallRecursive object.
        """
        self.inf = float('INF')
