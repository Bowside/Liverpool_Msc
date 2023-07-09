"""
This file contains the logic tests for the Floyd Warshall algorithm.

Author: Dillon Mantle
Date: 2023-07-05
"""
import unittest
from pathlib import Path
import sys
import os
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(SCRIPT_DIR))

# Import Floyd Warshall function
from floyd_warshall.recursive import FloydWarshallRecursive

# Import Floyd Warshall test cases
from test_cases import (test_a, test_b, test_c, test_d, test_e, test_f,
                        result_a, result_b, result_c, result_d, result_e, result_f)

class TestFloydWarshallRecursive(unittest.TestCase):

    def test_floyd_a(self):
        # Test Case 1: Shortest distance between all pairs of vertices
        self.assertEqual(floyd_warshall_recursive.calc_shortest_distance(test_a)
                         , result_a
                         , "Test A: Shortest distance result incorrect")

        # Test Case 2: Number of vertices in the graph
        self.assertEqual(floyd_warshall_recursive.vertex_count
                         ,  len(result_a)
                         , "Test A: Number of vertices incorrect")

    def test_floyd_b(self):
        # Test Case 1: Shortest distance between all pairs of vertices
        self.assertEqual(floyd_warshall_recursive.calc_shortest_distance(test_b)
                         , result_b
                         , "Test B: Shortest distance result incorrect")

        # Test Case 2: Number of vertices in the graph
        self.assertEqual(floyd_warshall_recursive.vertex_count
                            ,  len(result_b)
                            , "Test B: Number of vertices incorrect")

    def test_floyd_c(self):
        # Test Case 1: Shortest distance between all pairs of vertices
        self.assertEqual(floyd_warshall_recursive.calc_shortest_distance(test_c)
                         , result_c
                         , "Test C: Shortest distance result incorrect")

        # Test Case 2: Number of vertices in the graph
        self.assertEqual(floyd_warshall_recursive.vertex_count
                        , len(result_c)
                        , "Test C: Number of vertices incorrect")
        
    def test_floyd_d(self):
        # Test Case 1: Shortest distance between all pairs of vertices
        self.assertNotEquals(floyd_warshall_recursive.calc_shortest_distance(test_d)
                            , result_d
                            , "Test D: Shortest distance result incorrect")

        # Test Case 2: Number of vertices in the graph
        self.assertEqual(floyd_warshall_recursive.vertex_count
                        , len(result_d)
                        , "Test D: Number of vertices incorrect")
        
    def test_floyd_e(self):
        # Test Case 1: Shortest distance between all pairs of vertices
        self.assertEqual(floyd_warshall_recursive.calc_shortest_distance(test_e)
                         , result_e
                         , "Test E: Shortest distance result incorrect")

        # Test Case 2: Number of vertices in the graph
        self.assertEqual(floyd_warshall_recursive.vertex_count
                        , len(result_e)
                        , "Test E: Number of vertices incorrect")

    # If you want to make your CPU sweat, comment this in
    # def test_floyd_f(self):
    #     # Test Case 1: Shortest distance between all pairs of vertices
    #     self.assertEqual(floyd_warshall_recursive.calc_shortest_distance(test_f)
    #                     , result_f
    #                     , "Test F: Shortest distance result incorrect")
    #     # Test Case 2: Number of vertices in the graph
    #     self.assertEqual(floyd_warshall_recursive.vertex_count
    #                     , len(result_f)
    #                     , "Test F: Number of vertices incorrect")

    def test_read_graphfile(self):
        """
        Tests the read_graph method of FloydWarshallRecursive class.
        """
        floyd_warshall_recursive = FloydWarshallRecursive()
        relative_path = os.path.dirname(__file__)

        # Test Case 1: Valid graph file

        test_file = Path(relative_path, '../graphs/sample_1.txt')
        result_file = [[10, 2, 3, 6],
                           [8, 10, 1, 4],
                           [7, 9, 10, 3],
                           [4, 6, 7, 10]]
        test_graph = floyd_warshall_recursive.read_graphfile(test_file)
        self.assertEqual(floyd_warshall_recursive.calc_shortest_distance(test_graph)
                         , result_file
                         , "result incorrect")

if __name__ == '__main__':
    floyd_warshall_recursive = FloydWarshallRecursive()
    unittest.main()
