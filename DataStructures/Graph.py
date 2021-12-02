from typing import Any, List

MAXV = 1000


class AdjNode:
    Y: int = None
    Next: 'AdjNode' = None
    Weight: int = 0

    def __init__(self, y=None, next=None, weight=0):
        self.Y = y
        self.Next = next
        self.Weight = weight


class Graph:
    Edges: List[AdjNode]
    Degree: List[int]
    NVertices: int
    NEdges: int
    Directed: bool

    def __init__(self, directed: bool = False, MaxVertices: int = MAXV):
        self.Edges = [AdjNode] * MaxVertices
        self.Degree = [0] * MaxVertices
        self.NVertices = 0
        self.NEdges = 0
        self.Directed = directed

    def insert_edge(self, x: int, y: int, weight: int = 0, directed: bool = False):
        newEdge = AdjNode(y=y, weight=weight, next=self.Edges[x])
        self.Edges[x] = newEdge

        self.Degree[x] += 1

        if (directed == False):
            self.insert_edge(x=y, y=x, weight=weight, directed=True)
        else:
            self.NEdges += 1

    def read_graph(self, directed: bool = False):
        self.Directed = directed
        self.Degree = [0] * MAXV
        self.NVertices = int(input("Enter the number of vertices: "))
        self.NEdges = int(input("Enter the number of edges: "))

        for i in range(self.NEdges):
            x, y, weight = map(int, input(
                "Enter the edge (x, y , weight): ").split())
            self.insert_edge(x=x, y=y, weight=weight, directed=directed)

    def print_graph(self):
        for i in range(self.NVertices):
            print("Vertex: ", i, end="")
            while self.Edges[i].Y:
                print(" -> ", self.Edges[i].Y, " (",
                      self.Edges[i].Weight, ")", sep="", end="")
                self.Edges[i] = self.Edges[i].Next
            print()
