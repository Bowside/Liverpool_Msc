"""
A class that implements the Floyd-Warshall algorithm to find the shortest distances
between all pairs of vertices in a graph using a recursive approach.

Author: Dillon Mantle
Date: 2023-07-05
"""
class FloydWarshallRecursive:
    """
    A class that implements the Floyd-Warshall algorithm to find the shortest distances 
    between all pairs of vertices in a graph using a recursive approach.
    """

    def calc_shortest_distance(self, graph: list):
        """
        Applies the Floyd-Warshall algorithm recursively to find the shortest distances 
        between all pairs of vertices in a graph.

        Args:
            graph (List[List[float]]): The adjacency matrix representation of the graph.

        Returns:
            List[List[float]]: A 2D matrix representing the shortest distances between 
            all pairs of vertices.
        """

        # Detect the number of vertices in the graph
        dist = graph
        nV = len(graph)
        self.vertex_count = nV

        def iterator(sV, eV, k):
            """
            Recursive iterator function to calculate the shortest distance between two 
            vertices using intermediate vertices.

            Args:
                sV (int): The index of the starting vertex.
                eV (int): The index of the ending vertex.
                k (int): The intermediate vertex index to consider.

            Returns:
                float: The shortest distance between the starting vertex and the ending 
                vertex.
            """

            if k == -1:
                # Return weight when there are no intermediary vertices
                # This is when k == -1 since index 0 is first vertex
                return dist[sV][eV]
            else:
                # If travelling via k is shorter return shorter distance
                return min(iterator(sV, eV, k - 1),
                           iterator(sV, k, k - 1) + iterator(k, eV, k - 1))

        for k in range(nV):
            for sV in range(nV):
                for eV in range(nV):
                    dist[sV][eV] = iterator(sV, eV, k)

        return dist

    def read_graphfile(self, filename):
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
            nV, nE = map(int, lines[0].split())
            graph = [[self.inf] * nV for _ in range(nV)]
            for line in lines[1:]:
                sV, eV, weight = map(int, line.split())
                graph[sV][eV] = weight

            self.vertex_count = nV
            self.edge_count = nE

            return graph

    def __init__(self) -> None:
        """
        Initializes the FloydWarshallRecursive object.
        """
        self.inf = float('INF')
        self.vertex_count = 0
        self.edge_count = 0
