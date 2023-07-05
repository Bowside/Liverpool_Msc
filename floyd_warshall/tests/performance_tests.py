"""
This file containe a performance test for the Floyd Warshall algorithm.

Author: Dillon Mantle
Date: 2023-07-05
"""

import sys
import os
import cProfile
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(SCRIPT_DIR))

# Import Floyd Warshall function
from floyd_warshall.recursive import FloydWarshallRecursive

# Import Floyd Warshall test cases
from test_cases import (test_a, test_b, test_c, test_d)

floyd_warshall_recursive = FloydWarshallRecursive()

def run_performance_tests():
    """
    Runs performance tests using the Floyd-Warshall algorithm.

    This script imports the FloydWarshallRecursive class and test cases from the 
    'floyd_warshall' package. It initializes an instance of the FloydWarshallRecursive
    class and runs performance tests using the calc_shortest_distance method on the 
    provided test cases. The cProfile module is used to measure the execution time 
    and other performance metrics of the algorithm.

    Note:
        - The cProfile.run() function is used to profile the performance of the 
          calc_shortest_distance method.
        - Uncomment the last line if you want to run a more intensive performance test.

    Performance tests:
        - Test A: A small test case.
        - Test B: A medium test case.
        - Test C: A large test case.
        - Test D: An intensive test case (commented out by default).

    """
    cProfile.run("floyd_warshall_recursive.calc_shortest_distance(test_a)")

    cProfile.run("floyd_warshall_recursive.calc_shortest_distance(test_b)")

    cProfile.run("floyd_warshall_recursive.calc_shortest_distance(test_c)")

    # If you want to make your CPU sweat, comment this in
    # cProfile.run("floyd_warshall_recursive.calc_shortest_distance(test_d)")

if __name__ == '__main__':
    run_performance_tests()
