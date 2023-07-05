"""
Module Name: Floyd-Warshall Algorithm
Description: This module implements the Floyd-Warshall algorithm to find the shortest 
distances between all pairs of vertices in a graph.
Author: Dillon Mantle

Imports:
- pathlib.Path: A class representing the file path.
- os: A module providing a way to interact with the operating system.

Global Variables:
- INF (float): A constant representing infinity.

Functions:
- floyd_warshall_recursive: Applies the Floyd-Warshall algorithm recursively to find the
  shortest distances between all pairs of vertices in a graph.
- helper: Recursive helper function to calculate the shortest distance between two 
  vertices using intermediate vertices.
- read_graph: Reads a graph from a file and constructs its adjacency matrix 
  representation.
- main: The main entry point of the script that interacts with the user to read a graph 
  file, applies the Floyd-Warshall algorithm, and prints the resulting shortest distances
  between all pairs of vertices.
"""
# Imports
from pathlib import Path
import os

# Global variables
INF = float('INF')


def floyd_warshall_recursive(graph: list, num_vertices: int):
    """
    Applies the Floyd-Warshall algorithm recursively to find the shortest distances 
    between all pairs of vertices in a graph.

    Args:
        graph (List[List[float]]): The adjacency matrix representation of the graph.
        n (int): The number of vertices in the graph.

    Returns:
        List[List[float]]: A 2D matrix representing the shortest distances between 
        all pairs of vertices.
    """

    def helper(dist, k, i, j):
        """
        Recursive helper function to calculate the shortest distance between two 
        vertices using intermediate vertices.

        Args:
            dist (List[List[float]]): The current matrix of shortest distances.
            k (int): The intermediate vertex index to consider.
            i (int): The index of the starting vertex.
            j (int): The index of the ending vertex.

        Returns:
            float: The shortest distance between the starting vertex and the ending 
            vertex.
        """
        if k == 0:
            return dist[i][j]
        else:
            return min(helper(dist, k-1, i, j), helper(dist, k-1, i, k) + helper(dist, k-1, k, j))

    dist = [[INF] * num_vertices for _ in range(num_vertices)]

    for i in range(num_vertices):
        for j in range(num_vertices):
            dist[i][j] = graph[i][j]

    for k in range(num_vertices):
        for i in range( num_vertices):
            for j in range(num_vertices):
                dist[i][j] = helper(dist, k, i, j)

    return dist

def read_graph(filename):
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
        n, _ = map(int, lines[0].split())
        graph = [[INF] * n for _ in range(n)]
        for line in lines[1:]:
            u, v, weight = map(int, line.split())
            graph[u][v] = weight
        return graph, n

def main():
    """
    The main entry point of the script that interacts with the user to read a graph file
    , applies the Floyd-Warshall algorithm, and prints the resulting shortest distances 
    between all pairs of vertices.

    This function prompts the user to enter the relative path of the graph file. It 
    repeatedly prompts the user until a valid file is provided or the user chooses to 
    quit by entering 'q'. Once a valid file is provided, it reads the file, applies the
    Floyd-Warshall algorithm to find the shortest distances, and prints the result.

    Raises:
        ValueError: If the specified file does not exist.
    """
    relative_path = os.path.dirname(__file__)
    while True:
        user_input = input("Enter the relative path of your file, or 'q' to quit: ")
        if user_input == 'q':
            break
        try:
            filepath = Path(relative_path, user_input)
            print(filepath)
            if filepath.exists():
                graph, num_vertices = read_graph(filepath)
                result = floyd_warshall_recursive(graph, num_vertices)
                print(f'{filepath.name}: {result}')
            if not filepath.exists():
                raise ValueError
        except ValueError:
            print(f"Invalid file {relative_path}, press 'q' to quit or try again.")
            
if __name__ == '__main__':
    main()