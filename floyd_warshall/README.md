# Floyd-Warshall algorithm, recursively
The Floyd-Warshall algorithm is typically implemented using dynamic programming rather than recursion due to its efficiency. 
Keep in mind that this recursive implementation has exponential time complexity, ie it's slow af and should never be used.

This implementation assumes that the graph is represented as an adjacency matrix, where graph[i][j] represents the weight of the edge from vertex i to vertex j. The n parameter represents the number of vertices in the graph.

## Installation
Clone the repo and copy the floyd_warshall directory and contents into your project.
There are no specific depedencies.

If you buy me beer I will create a PyPi package.

## Usage
To use the function you need to import it into your script.
```python
from floyd_warshall.recursive import FloydWarshallRecursive

# Use value for infinity to denote edges that do not exist
INF = float('INF')

# Add weights into a list with graph[i][j] meaning "the direct weight from i to j" 
# assuming each vertex is numbered consecutively from 0
graph = [[INF, 2, 5, INF], 
        [INF, INF, 1, 6], 
        [INF, INF, INF, 3], 
        [4, INF, INF, INF]]

# Returns output
floyd_warshall_recursive = FloydWarshallRecursive()
floyd_warshall_recursive.calc_shortest_distance(test_a)

# Example output
output = [[-8, -6, -5, -12],  
          [-10, -8, -7, -14], 
          [-1, 1, 2, -5],
          [-12, -10, -9, -16]]

# You can also load a graph file
# Example files are in the /graphs folder
graph = floyd_warshall_recursive.read_graphfile(test_file)
vertex_count = floyd_warshall_recursive.vertex_count
edge_count = floyd_warshall_recursive.edge_count
```

## Running Unit Tests
To run the unit tests use the following in the terminal for the test_cases.py file.
```bash
python tests/unit_tests.py
```

## Running Performance Tests
To run the performance tests use the following in the terminal for the test_cases.py file.
```bash
python tests/performance_tests.py
``

