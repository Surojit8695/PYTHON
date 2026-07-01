# -------------------------------------------------------------
# Question:
# Write a program in Python to create a Graph class to store and
# manipulate graphs. Perform the following functions:
# (a) Read an edge list file, where each edge (u, v) appears exactly once.
# (b) Print the degree information of each node.
# Consider the graph as undirected and unweighted.
# -------------------------------------------------------------

class Graph:

    def __init__(self):
        # Dictionary to store adjacency list
        self.graph = {}

    # Add an edge to the graph
    def add_edge(self, u, v):

        if u not in self.graph:
            self.graph[u] = []

        if v not in self.graph:
            self.graph[v] = []

        self.graph[u].append(v)
        self.graph[v].append(u)

    # Read graph from file
    def read_file(self, filename):

        with open(filename, "r") as file:

            for line in file:
                u, v = line.split()
                self.add_edge(u, v)

    # Print degree of every node
    def print_degree(self):

        print("\nDegree of each node:")

        for node in self.graph:
            print(node, ":", len(self.graph[node]))


# Driver Code
g = Graph()

filename = input("Enter edge list file name: ")

g.read_file(filename)

g.print_degree()