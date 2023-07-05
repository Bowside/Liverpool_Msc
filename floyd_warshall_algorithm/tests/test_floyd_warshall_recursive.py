"""
Module Name: Floyd-Warshall Algorithm - Test
Description: This module contains test cases for the Floyd-Warshall algorithm.
Author: Dillon Mantle
"""

import unittest
from io import StringIO
from contextlib import redirect_stdout
from pathlib import Path
from floyd_warshall import read_graph, floyd_warshall_recursive

class FloydWarshallTestCase(unittest.TestCase):
    def test_read_graph(self):
        # Test case 1
        graph, num_vertices = read_graph('test_graph.txt')
        expected_graph = [
            [0, 5, 10, float('inf')],
            [float('inf'), 0, 3, float('inf')],
            [float('inf'), float('inf'), 0, 1],
            [float('inf'), 2, float('inf'), 0]
        ]
        expected_num_vertices = 4
        self.assertEqual(graph, expected_graph)
        self.assertEqual(num_vertices, expected_num_vertices)

        # Test case 2
        graph, num_vertices = read_graph('test_graph_empty.txt')
        expected_graph = []
        expected_num_vertices = 0
        self.assertEqual(graph, expected_graph)
        self.assertEqual(num_vertices, expected_num_vertices)

    def test_floyd_warshall_recursive(self):
        graph = [
            [0, 5, 10, float('inf')],
            [float('inf'), 0, 3, float('inf')],
            [float('inf'), float('inf'), 0, 1],
            [float('inf'), 2, float('inf'), 0]
        ]
        num_vertices = 4
        expected_result = [
            [0, 5, 8, 9],
            [float('inf'), 0, 3, 4],
            [float('inf'), float('inf'), 0, 1],
            [float('inf'), 2, 5, 0]
        ]
        result = floyd_warshall_recursive(graph, num_vertices)
        self.assertEqual(result, expected_result)

    def test_main(self):
        # Prepare input
        user_input = 'test_graph.txt\nq\n'
        expected_output = 'Enter the relative path of your file, or \'q\' to quit: test_graph.txt\n'
        expected_output += 'test_graph.txt: [[0, 5, 8, 9], [inf, 0, 3, 4], [inf, inf, 0, 1], [inf, 2, 5, 0]]\n'
        expected_output += 'Enter the relative path of your file, or \'q\' to quit: q\n'

        # Capture stdout
        with StringIO() as buffer, redirect_stdout(buffer):
            # Mock user input
            with unittest.mock.patch('builtins.input', side_effect=user_input):
                # Run the main function
                main()

            # Get the output
            output = buffer.getvalue()

        # Compare output
        self.assertEqual(output, expected_output)


if __name__ == '__main__':
    unittest.main()