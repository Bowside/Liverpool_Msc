"""
An implementation of the Floyd-Warshall algorithm using a recursive approach.

Author: Dillon Mantle, 2023-07-05
"""
import os
from pathlib import Path
from floyd_warshall_recursive import FloydWarshallRecursive

def main():
    """
    The main entry point of the script. Prompts the user to enter the relative path of 
    a graph file and applies the Floyd-Warshall algorithm to find the shortest distances
    between all pairs of vertices.

    This function repeatedly prompts the user until a valid file is provided or the user
    chooses to quit by entering 'q'. Once a valid file is provided, it initializes the 
    Floyd-Warshall algorithm, reads the graph from the file, calculates the shortest 
    distances, and prints the result.

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
                # Initialise the Floyd-Warshall algorithm
                floyd_warshall_recursive = FloydWarshallRecursive()
                # Read the graph from the file
                graph, num_vertices = floyd_warshall_recursive.read_graph(filepath)
                # Calculate the shortest distances between all pairs of vertices
                result = floyd_warshall_recursive.calc_shortest_distance(graph, num_vertices)
                print(f'{filepath.name}: {result}')
            if not filepath.exists():
                raise ValueError
        except ValueError:
            print(f"Invalid file {relative_path}, press 'q' to quit or try again.")

if __name__ == '__main__':
    main()
