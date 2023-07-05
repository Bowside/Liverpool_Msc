# This class defines the methods required for the floyd warshall algorithm
# It also contains the main method which is used to run the program.
# The program takes in a text file which contains the graph and the weights
# of the edges. The program then runs the floyd warshall algorithm on the
# graph and prints out the shortest path between all the nodes in the graph.
# The program also prints out the shortest path between two nodes in the
# graph if the user enters the two nodes.

# Creating a class for the floyd warshall algorithm
class FloydWarshallAlgorithm:
    # Constructor for the class
    def __init__(self):
        # Declaring the variables that will be used in the program
        self.graph = []
        self.nodes = []
        self.edges = []
        self.distances = []
        self.path = []
        self.num_nodes = 0
        self.num_edges = 0
        self.infin = 999999999
        self.start_node = 0
        self.end_node = 0
        self.filename = ''

    # This method is used to read in the text file and store the graph
    # in a 2D array
    def read_file(self, file_name):
        # Opening the text file
        file = open(file_name, "r")
        line = file.readline()

        # Storing the number of nodes and edges in the graph
        #self.num_nodes = int(line[0])
        #self.num_edges = int(line[1])
        # Reading in the rest of the lines in the text file
        for line in file:
            # Splitting the line into a list
            line = line.split(',')
            # Storing the nodes and edges in the graph
            self.nodes.append(int(line[0]))
            self.edges.append(int(line[1]))
            # Creating a list to store the weights of the edges
            weights = []
            # Looping through the rest of the line
            for i in range(2, len(line)):
                # Storing the weights in the list
                weights.append(int(line[i]))
            # Storing the weights in the graph
            self.graph.append(weights)
        # Closing the text file
        file.close()

        # Count number of nodes
        self.num_nodes = len(set(self.nodes))
        # count number of edges
        self.num_edges = len(self.edges)

    # This method is used to run the floyd warshall algorithm on the graph
    def floyd_warshall(self):
        # Creating a list to store the distances between the nodes
        self.distances = self.graph
        # Creating a list to store the path between the nodes
        self.path = self.graph
        # Looping through the nodes
        for k in range(self.num_nodes):
            # Looping through the nodes
            for i in range(self.num_nodes):
                # Looping through the nodes
                for j in range(self.num_nodes):
                    # Checking if the distance between the nodes is less than
                    # the distance between the nodes through the other node
                    if self.distances[i][k] + self.distances[k][j] < self.distances[i][j]:
                        # Storing the distance between the nodes
                        self.distances[i][j] = self.distances[i][k] + self.distances[k][j]
                        # Storing the path between the nodes
                        self.path[i][j] = self.path[i][k]

    # This method is used to print out the shortest path between all the nodes
    # in the graph
    def print_shortest_path(self):
        # Looping through the nodes
        for i in range(self.num_nodes):
            # Looping through the nodes
            for j in range(self.num_nodes):
                # Checking if the distance between the nodes is infinity
                if self.distances[i][j] == self.infin:
                    # Printing out the infinity value
                    print("INF", end=" ")
                # Checking if the distance between the nodes is not infinity
                else:
                    # Printing out the distance between the nodes
                    print(self.distances[i][j], end=" ")
            # Printing out a new line
            print()

    # This method is used to print out the shortest path between two nodes
    # in the graph
    def print_path(self):
        # Checking if the distance between the nodes is infinity
        # if self.distances[self.start_node][self.end_node] == self.infin:
        #     # Printing out the infinity value
        #     print("INF")
        # # Checking if the distance between the nodes is not infinity
        # else:
            # Storing the start node
            start = self.start_node
            # Storing the end node
            end = self.end_node
            # Creating a list to store the path between the nodes
            path = []
            # Looping through the nodes
            while start != end:
                # Storing the start node
                start = self.path[start][end]
                # Storing the start node in the list
                path.append(start)
            # Printing out the start node
            print(self.start_node, end=" ")
            # Looping through the list
            for i in range(len(path)):
                # Printing out the node in the list
                print(path[i], end=" ")
            # Printing out the end node
            print(self.end_node)

    # This method is used to run the program
    def main(self, filename: str):
        # Reading in the text file
        self.read_file(filename)
        # Running the floyd warshall algorithm
        self.floyd_warshall()
        # Checking if the user entered two nodes
        # if len(sys.argv) == 4:
        #     # Storing the start node
        #     self.start_node = int(sys.argv[2])
        #     # Storing the end node
        #     self.end_node = int(sys.argv[3])
        #     # Printing out the shortest path between the two nodes
        self.print_path()
        # Checking if the user did not enter two nodes
        # else:
        #     # Printing out the shortest path between all the nodes
        #     self.print_shortest_path()