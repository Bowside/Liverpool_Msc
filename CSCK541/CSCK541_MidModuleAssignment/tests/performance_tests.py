"""
This file contains a performance test for the imperative and iterative
implementations of the Floyd Warshall algorithm.

Author: Dillon Mantle
Date: 2023-07-05
"""

import sys
import os
import cProfile
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(SCRIPT_DIR))

# Import Floyd Warshall modules
from floyd_warshall.recursive import FloydWarshallRecursive
from floyd_warshall.imperative import FloydWarshallImperative

# Import Floyd Warshall test cases
from test_cases import (test_a, test_b, test_c, test_d, test_e, test_f)

floyd_warshall_recursive = FloydWarshallRecursive()
floyd_warshall_imperative = FloydWarshallImperative()

def run_performance_tests():
    """
    Runs performance tests using the Floyd-Warshall algorithm.

    The cProfile module is used to measure the execution time 
    and other performance metrics of the algorithm.

    Note:
        - The cProfile.run() function is used to profile the performance of the 
          calc_shortest_distance method.
        - Uncomment the last line if you want to run a more intensive performance test.

    Performance tests:
        - Test A: A small test case.
        - Test E: A medium test case.
        - Test F: An intensive test case.
    """
    # Declartive performance tests
    cProfile.run("floyd_warshall_recursive.calc_shortest_distance(test_a)")
    cProfile.run("floyd_warshall_recursive.calc_shortest_distance(test_e)")
    # If you have time to kill, comment this in
    # cProfile.run("floyd_warshall_recursive.calc_shortest_distance(test_f)")

    # Imperative performance tests
    cProfile.run("floyd_warshall_imperative.calc_shortest_distance(test_a)")
    cProfile.run("floyd_warshall_imperative.calc_shortest_distance(test_e)")
    # If you have time to kill, comment this in
    # cProfile.run("floyd_warshall_imperative.calc_shortest_distance(test_f)")

if __name__ == '__main__':
    run_performance_tests()
