# Program 1(Incomplete preparation)
# Write a Python program to create a Graph class.
# (a) Read graph as edge list from a file.
# (b) Print the neighbours of each vertex.
# (c) Display a message if there is no pendant vertex.

class Graph:

    def __init__(self):
        self.graph = {}

    def read_graph(self, filename):
        file = open(filename, "r")

        for line in file:
            u, v = line.split()

            if u not in self.graph:
                self.graph[u] = []

            if v not in self.graph:
                self.graph[v] = []

            self.graph[u].append(v)
            self.graph[v].append(u)

        file.close()

    def neighbours(self):
        print("\nNeighbours of each vertex:")
        for vertex in self.graph:
            print(vertex, ":", self.graph[vertex])

    def pendant_vertex(self):
        found = False

        for vertex in self.graph:
            if len(self.graph[vertex]) == 1:
                print(vertex, "is a pendant vertex")
                found = True

        if not found:
            print("No pendant vertex exists.")


g = Graph()

filename = input("Enter file name: ")
g.read_graph(filename)

g.neighbours()
g.pendant_vertex()