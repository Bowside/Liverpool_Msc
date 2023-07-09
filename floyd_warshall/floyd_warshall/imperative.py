"""
A class that implements the Floyd-Warshall algorithm to find the shortest distances
between all pairs of vertices in a graph using an imperative approach.

Author: Dillon Mantle
Date: 2023-07-05
Dapted from: https://www.geeksforgeeks.org/floyd-warshall-algorithm-dp-16/
"""
class FloydWarshallImperative:
    """
    A class that implements the Floyd-Warshall algorithm to find the shortest distances 
    between all pairs of vertices in a graph using an imperative approach.
    """

    def calc_shortest_distance(self, graph: list):
        """
        Applies the Floyd-Warshall algorithm imperatively to find the shortest distances 
        between all pairs of vertices in a graph.

        Args:
            graph (List[List[float]]): The adjacency matrix representation of the graph.

        Returns:
            List[List[float]]: A 2D matrix representing the shortest distances between 
            all pairs of vertices.
        """

        # initializing the solution matrix same as input graph matrix
        # OR we can say that the initial values of shortest distances
        # are based on shortest paths considering no intermediate vertices
        dist = list(map(lambda i: list(map(lambda j: j, i)), graph))
    
        # Detect the number of vertices in the graph
        nV = len(graph)
        self.vertex_count = nV

        # Add all vertices one by one to the set of intermediate vertices.
        # ---> Before start of an iteration, we have shortest distances between all 
        # pairs of vertices such that the shortest distances consider only the vertices
        # in the set {0, 1, 2, .. k-1} as intermediate vertices.
        # ----> After the end of a iteration, vertex no. k is added to the set of 
        # intermediate vertices and the set becomes {0, 1, 2, .. k}
        for k in range(nV):
            # pick all vertices as source one by one
            for sV in range(nV):
                # Pick all vertices as destination for the
                # above picked source
                for eV in range(nV):
    
                    # If vertex k is on the shortest path from
                    # i to j, then update the value of dist[i][j]
                    dist[sV][eV] = min(dist[sV][eV],
                                    dist[sV][k] + dist[k][eV]
                                    )

            return dist

    def __init__(self) -> None:
        """
        Initializes the FloydWarshallRecursive object.
        """
        self.inf = float('INF')
        self.vertex_count = 0
        self.edge_count = 0
