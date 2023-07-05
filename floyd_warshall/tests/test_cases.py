""" 
This file contains four different test cases for the Floyd Warshall
algorithm function. Below is the expected inputs and outputs for each
different scenario.

Author: Dillon Mantle
Date: 2023-07-05
"""

# Use value for infinity to denote edges that do not exist
INF = float('INF')

# Test A: Simple Graph (Three Vertices)
test_a = [[0, 1, INF],
            [1, 0, 3],
            [INF, 3, 0]]

result_a = [[0, 1, 4],
            [1, 0, 3],
            [4, 3, 0]]

# Test B: Simple Graph, Negative Edges Graph (No Negative Cycles)
test_b = [[0, 1, -2, INF],
            [1, 0, INF, 3],
            [2, INF, 0, INF],
            [INF, -3, INF, 0]]

result_b = [[0, 1, -2, 4],
            [1, 0, -1, 3],
            [2, 3, 0, 6],
            [-2, -3, -4, 0]]


# Test C: Large Graph (Eight Vertices)
test_c = [[0, 8, INF, INF, 5, 3, INF, INF],
            [INF, 0, INF, 11, 5, INF, 9, INF],
            [7, 4, 0, INF, INF, 4, INF, INF],
            [INF, INF, INF, 0, 1, INF, INF, 2],
            [INF, INF, INF, INF, 0, INF, INF, INF],
            [INF, INF, INF, INF, INF, 0, INF, INF],
            [INF, INF, INF, 3, INF, INF, 0, 12],
            [INF, INF, INF, INF, INF, INF, INF, 0]]

result_c = [[0 ,8 ,INF ,19 ,5 ,3 ,17 ,21],
            [INF ,0 ,INF ,11 ,5 ,INF ,9 ,13],
            [7 ,4 ,0 ,15 ,9 ,4 ,13 ,17],
            [INF ,INF ,INF ,0 ,1 ,INF ,INF ,2],
            [INF ,INF ,INF ,INF ,0 ,INF ,INF ,INF],
            [INF ,INF ,INF ,INF ,INF ,0 ,INF ,INF],
            [INF ,INF ,INF ,3 ,4 ,INF ,0 ,5],
            [INF ,INF ,INF ,INF ,INF ,INF ,INF ,0]]

# Test D: Very Large Graph (Sixteen Vertices)
test_d = [[0, 8, INF, INF, 5, 3, INF, INF, 2, INF, 4, INF, INF, 6, INF, 1],
          [INF, 0, INF, 11, INF, INF, 9, INF, INF, 6, INF, INF, INF, INF, 7, INF],
          [INF, INF, 0, INF, 3, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF],
          [4, INF, 7, 0, INF, INF, INF, 5, INF, INF, 6, 2, INF, INF, INF, INF],
          [4, 4, 8, INF, 0, INF, INF, INF, INF, 4, INF, 11, 5, INF, 9, INF],
          [4, 4, 8, INF, INF, 0, INF, INF, 7, 4, 9, INF, INF, 4, INF, INF],
          [4, 4, 8, 3, INF, 2, 0, 12, INF, INF, INF, INF, INF, INF, INF, 12],
          [4, 4, 8, INF, INF, INF, INF, 0, 5, 2, 9, 22, 3, 7, 9, 1],
          [2, 8, 8, INF, 5, 3, INF, INF, 0, 2, 8, 11, 23, 17, 1, 2],
          [INF, 5, INF, 11, 5, INF, 9, INF, INF, 0, INF, 1, 4, 11, INF, 8],
          [7, 4, 2, INF, INF, 4, INF, INF, 5, 3, 0, INF, 5, 2, 8, 11],
          [INF, 7, 4, INF, 1, 2, 9, 2, INF, INF, INF, 0, INF, INF, INF, 3],
          [INF, 7, 4, 11, 2, INF, INF, 3, 5, 4, INF, 11, 0, INF, 9, INF],
          [INF, 7, 4, INF, INF, 9, INF, INF, 7, 4, 9, INF, INF, 0, INF, INF],
          [INF, 7, 4, 3, INF, INF, 8, 12, INF, 6, INF, INF, INF, INF, 0, 12],
          [INF, 7, 4, INF, INF, INF, INF, 1, 5, 2, INF, 22, 3, 7, 9, 0]]

result_d = [[0 ,6 ,5 ,6 ,5 ,3 ,11 ,2 ,2 ,3 ,4 ,4 ,4 ,6 ,3 ,1],
            [12 ,0 ,11 ,10 ,8 ,9 ,9 ,9 ,14 ,6 ,16 ,7 ,10 ,13 ,7 ,10],
            [7 ,7 ,0 ,13 ,3 ,10 ,16 ,9 ,9 ,7 ,11 ,8 ,8 ,13 ,10 ,8],
            [4 ,7 ,6 ,0 ,3 ,4 ,11 ,4 ,6 ,6 ,6 ,2 ,7 ,8 ,7 ,5],
            [4 ,4 ,8 ,10 ,0 ,7 ,13 ,6 ,6 ,4 ,8 ,5 ,5 ,10 ,7 ,5],
            [4 ,4 ,8 ,10 ,6 ,0 ,13 ,6 ,6 ,4 ,8 ,5 ,8 ,4 ,7 ,5],
            [4 ,4 ,8 ,3 ,6 ,2 ,0 ,6 ,6 ,6 ,8 ,5 ,8 ,6 ,7 ,5],
            [4 ,4 ,5 ,9 ,4 ,5 ,11 ,0 ,5 ,2 ,8 ,3 ,3 ,7 ,6 ,1],
            [2 ,7 ,5 ,4 ,4 ,3 ,9 ,3 ,0 ,2 ,6 ,3 ,5 ,7 ,1 ,2],
            [6 ,5 ,5 ,11 ,2 ,3 ,9 ,3 ,8 ,0 ,10 ,1 ,4 ,7 ,9 ,4],
            [7 ,4 ,2 ,9 ,5 ,4 ,12 ,6 ,5 ,3 ,0 ,4 ,5 ,2 ,6 ,7],
            [5 ,5 ,4 ,11 ,1 ,2 ,9 ,2 ,7 ,4 ,9 ,0 ,5 ,6 ,8 ,3],
            [6 ,6 ,4 ,9 ,2 ,7 ,13 ,3 ,5 ,4 ,10 ,5 ,0 ,10 ,6 ,4],
            [9 ,7 ,4 ,11 ,6 ,7 ,13 ,7 ,7 ,4 ,9 ,5 ,8 ,0 ,8 ,8],
            [7 ,7 ,4 ,3 ,6 ,7 ,8 ,7 ,9 ,6 ,9 ,5 ,10 ,11 ,0 ,8],
            [5 ,5 ,4 ,9 ,4 ,5 ,11 ,1 ,5 ,2 ,9 ,3 ,3 ,7 ,6 ,0]]
