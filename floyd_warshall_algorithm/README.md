# Floyd-Warshall algorithm, recursively

The Floyd-Warshall algorithm is typically implemented using dynamic programming rather than recursion due to its efficiency. 
Keep in mind that this recursive implementation has exponential time complexity, so it is likely inefficient for large graphs. It is strongly recommended to use the iterative version of the Floyd-Warshall algorithm for practical purposes.

This implementation assumes that the graph is represented as an adjacency matrix, where graph[i][j] represents the weight of the edge from vertex i to vertex j. The n parameter represents the number of vertices in the graph.

