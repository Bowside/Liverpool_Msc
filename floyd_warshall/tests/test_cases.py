""" 
This file contains four different test cases for the Floyd Warshall
algorithm function. Below is the expected inputs and outputs for each
different scenario.

Author: Dillon Mantle
Date: 2023-07-05
"""

# Use value for infinity to denote edges that do not exist
INF = float('INF')

# Test A: Simple Graph (Four Vertices)
test_a = [[0, 1, INF, 1],
          [1, 0, 1, INF],
          [INF, 1, 0, 1],
          [1, INF, 1, 0]]

result_a = [[0, 1, 2, 1],
            [1, 0, 1, 2],
            [2, 1, 0, 1],
            [1, 2, 1, 0]]

# Test B: Negative Edges Graph, no negative cycles (Four Vertices)
test_b = [[0, INF, 9, INF],
            [INF, 0, INF, INF],
            [INF, -5, 0, 8],
            [-3, 2, INF, 0]]

result_b = [[0, 4, 9, 17],
            [INF, 0, INF, INF],
            [5, -5, 0, 8],
            [-3, 1, 6, 0]]

# Test C: Disconnected Verticies Graph (Four Vertices)
test_c = [[0, 1, INF, INF],
          [1, 0, INF, INF],
          [INF, INF, 0, 1],
          [INF, INF, 1, 0]]

result_c = [[0, 1, INF, INF],
            [1, 0, INF, INF],
            [INF, INF, 0, 1],
            [INF, INF, 1, 0]]

# Test D: Negative Cycle Graph (Four Vertices)
# This should fail as the graph contains a negative cycle
test_d = [[0, 1, INF, 1],
          [1, 0, 1, INF],
          [INF, 1, 0, -2],
          [1, INF, -2, 0]]

result_d = [[0, -1, -2, -3],
            [1, 0, -1, -2],
            [-2, -1, 0, -1],
            [-1, -2, -1, 0]]

# Test E: Large Graph (Eight Vertices)
test_e = [[0, 8, INF, INF, 5, 3, INF, INF],
            [INF, 0, INF, 11, 5, INF, 9, INF],
            [7, 4, 0, INF, INF, 4, INF, INF],
            [INF, INF, INF, 0, 1, INF, INF, 2],
            [INF, INF, INF, INF, 0, INF, INF, INF],
            [INF, INF, INF, INF, INF, 0, INF, INF],
            [INF, INF, INF, 3, INF, INF, 0, 12],
            [INF, INF, INF, INF, INF, INF, INF, 0]]

result_e = [[0 ,8 ,INF ,19 ,5 ,3 ,17 ,21],
            [INF ,0 ,INF ,11 ,5 ,INF ,9 ,13],
            [7 ,4 ,0 ,15 ,9 ,4 ,13 ,17],
            [INF ,INF ,INF ,0 ,1 ,INF ,INF ,2],
            [INF ,INF ,INF ,INF ,0 ,INF ,INF ,INF],
            [INF ,INF ,INF ,INF ,INF ,0 ,INF ,INF],
            [INF ,INF ,INF ,3 ,4 ,INF ,0 ,5],
            [INF ,INF ,INF ,INF ,INF ,INF ,INF ,0]]

# Test F: Very Large Graph (Twelve Vertices)
test_f = [[0, 1, INF, INF, 1, INF, INF, INF, INF, INF, INF, INF],
          [1, 0, 1, INF, INF, 1, INF, INF, INF, INF, INF, INF],
          [INF, 1, 0, 1, INF, INF, 1, INF, INF, INF, INF, INF],
          [INF, INF, 1, 0, INF, INF, INF, 1, INF, INF, INF, INF],
          [1, INF, INF, INF, 0, 1, INF, INF, INF, INF, INF, INF],
          [INF, 1, INF, INF, 1, 0, 1, INF, INF, INF, INF, INF],
          [INF, INF, 1, INF, INF, 1, 0, 1, INF, INF, INF, INF],
          [INF, INF, INF, 1, INF, INF, 1, 0, 1, INF, INF, INF],
          [INF, INF, INF, INF, INF, INF, INF, 1, 0, 1, INF, INF],
          [INF, INF, INF, INF, INF, INF, INF, INF, 1, 0, 1, INF],
          [INF, INF, INF, INF, INF, INF, INF, INF, INF, 1, 0, 1],
          [INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, 1, 0]]

result_f = [[0, 1, 2, 3, 1, 2, 3, 4, 5, 6, 7, 8],
            [1, 0, 1, 2, 2, 1, 2, 3, 4, 5, 6, 7],
            [2, 1, 0, 1, 3, 2, 1, 2, 3, 4, 5, 6],
            [3, 2, 1, 0, 4, 3, 2, 1, 2, 3, 4, 5],
            [1, 2, 3, 4, 0, 1, 2, 3, 4, 5, 6, 7],
            [2, 1, 2, 3, 1, 0, 1, 2, 3, 4, 5, 6],
            [3, 2, 1, 2, 2, 1, 0, 1, 2, 3, 4, 5],
            [4, 3, 2, 1, 3, 2, 1, 0, 1, 2, 3, 4],
            [5, 4, 3, 2, 4, 3, 2, 1, 0, 1, 2, 3],
            [6, 5, 4, 3, 5, 4, 3, 2, 1, 0, 1, 2],
            [7, 6, 5, 4, 6, 5, 4, 3, 2, 1, 0, 1],
            [8, 7, 6, 5, 7, 6, 5, 4, 3, 2, 1, 0]]
