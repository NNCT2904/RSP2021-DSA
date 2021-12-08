from ..DataStructures.Graph import Graph

discovered = [False] * 1001
processed = [False] * 1001
parent = [-1] * 1001
entrytime = [0] * 1001
stack = []
time = 0
finished = False

def DFS(graph: Graph, start: int):
    discovered[start] = True
    currentEdgeNode = graph.Edges[start]
    processVertexEarly(start)

    while (currentEdgeNode != None):
        sucessor = currentEdgeNode.Y
        if (discovered[sucessor] == False):
            parent[sucessor] = start
            processEdge(start, sucessor)
            DFS(graph, sucessor)
        elif (processed[sucessor] == False or graph.directed):
            processEdge(start, sucessor)
            currentEdgeNode = currentEdgeNode.Next
        processVertexLate(start)
        processed[start] = True


def processVertexEarly(vertex: int):
    pass


def processEdge(currentVertex: int, sucessor: int):
    pass


def processVertexLate(vertex: int):
    pass