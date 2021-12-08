from ..DataStructures.Graph import Graph


def BFS(graph: Graph, start:int):
    processed = [False] * graph.NVertices
    discovered = [False] * graph.NVertices
    parent = [-1] * graph.NVertices

    visited = [False] * graph.NVertices
    queue = []

    visited[start] = True
    queue.append(start)

    while queue:
        currentVertex = queue.pop(0)
        processVertexEarly(currentVertex)
        processed[currentVertex] = True
        p = graph.Edges[currentVertex]

        while p:
            sucessor = p.Y
            if (processed[sucessor] == False or graph.directed):
                processEdge(currentVertex, sucessor)
            if (discovered[sucessor] == False):
                queue.append(sucessor)
                discovered[sucessor] = True
                parent[sucessor] = currentVertex
            p = p.Next
        processVertexLate(currentVertex)


def processVertexEarly(vertex: int):
    pass


def processEdge(currentVertex: int, sucessor: int):
    pass


def processVertexLate(vertex: int):
    pass