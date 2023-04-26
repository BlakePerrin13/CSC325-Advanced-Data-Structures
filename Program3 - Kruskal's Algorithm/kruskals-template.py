import sys
from queue import Queue

class Graph:

    def __init__(self):
        self.verList = {}
        self.numVertices = 0

    class __Vertex:
        def __init__(self, key):
            self.id = key       
            self.connectedTo = {} 

        def getId(self):
            return self.id

        def getConnections(self):
            return self.connectedTo.keys()

        def getWeight(self, nbr):
            return self.connectedTo[nbr] 

        def addNeighbor(self, nbr, weight = 0):
            self.connectedTo[nbr] = weight

        def __str__(self):
            return f"connected to: {str([x.id for x in self.connectedTo])}"   

    def addVertex(self, key):
        self.numVertices += 1
        newVertex = Graph.__Vertex(key)
        self.verList[key] = newVertex 
        return newVertex

    def getVertex(self, n):
        if n in self.verList:
            return self.verList[n]
        else:
            return None

    def __contains__(self, n):
        return n in self.verList

    def addEdge(self, source, destination, weight = 0):
        if source not in self.verList:
            newVertex = self.addVertex(source)
        if destination not in self.verList:
            newVertex = self.addVertex(destination)
        self.verList[source].addNeighbor(self.verList[destination], weight)
    
    def getVertices(self):
        return self.verList.keys()

    def __iter__(self):
        return iter(self.verList.values())

    def dfs(self, s, visited = None):
        if visited is None:
            visited = set()

        if s not in visited:
            print(s, end = " ")
            visited.add(s)
            for next_node in [x.id for x in self.verList[s].connectedTo]:
                self.dfs(next_node, visited)        

    def bfs(self, s, visited = None):
        if visited is None:
            visited = set()

        q = Queue()
        q.put(s)
        visited.add(s)

        while not q.empty():
            current_node = q.get()
            print(current_node, end = " ")

            for next_node in [x.id for x in self.verList[current_node].connectedTo]:
                if next_node not in visited:
                    q.put(next_node)
                    visited.add(next_node)

    def kruskals(self):
        vertices_sets = set()
        edges_dict = dict()
        MST = set()
        
        ### WRITE YOUR CODE HERE ###
        # Create a set for each vertex in the graph and add it to the vertices_sets set
        for v in self.verList:
            vertices_sets.add(frozenset([v]))
        
        # Create a dictionary of edges and their weights
        for v in self.verList:
            for e in self.verList[v].connectedTo:
                edges_dict[(v, e.id)] = self.verList[v].connectedTo[e]

        # Sort the edges dictionary by weight
        # I found this code at: https://stackoverflow.com/questions/613183/how-do-i-sort-a-dictionary-by-value
        # The code first converts the dictionary to a list of tuples containing the edges and their weights.
        # It then sorts the list of tuples by the weight of the edges.
        # Then it returns the list of tuples containing the edges and their weights.
        # Because it returns a list of tuples, I converted it back to a dictionary
        edges_dict = {k: v for k, v in sorted(edges_dict.items(), key = lambda x: x[1])}

        # Loop through the edges dictionary.
        for e in edges_dict.keys():
            # For each vertices set, check if the edge's vertices are in the set.
            for v in vertices_sets:
                # If the first vertex of the edge is in one of the a sets of vertices, assign the set containing the vertex to v1.
                if e[0] in v:
                    v1 = v
                
                # If the second vertex of the edge is in one of the sets of vertices, assign the set containing the vertex to v2.
                if e[1] in v:
                    v2 = v
            
            # If the two sets are not the same, add the edge and its weight to the MST and merge the two sets.
            if v1 != v2:
                MST.add((e, edges_dict[e]))
                vertices_sets.remove(v1)
                vertices_sets.remove(v2)
                vertices_sets.add(v1.union(v2))

        return MST

def main():
    
    # create an empty graph
    graph = Graph()

    # get graph vertices & edges from input file and add them to the graph
    file = open(sys.argv[1], "r")
    for line in file:
        values = line.split()
        graph.addEdge(int(values[0]), int(values[1]), int(values[2]))
        graph.addEdge(int(values[1]), int(values[0]), int(values[2]))   

    # print adjacency list representation of the graph
    print()

    ### WRITE YOUR CODE HERE ###
    print("Graph adjacency list:")

    # Loop through the vertices in the graph and print the vertex and its connected vertices
    for v in graph.verList:
        print("{} connected to: {}".format(v, [x.id for x in graph.verList[v].connectedTo]))
    
    # create graph MST
    MST = graph.kruskals()
    # print graph MST
    print()    
    print("Graph MST:")
    print("Edge\t\tWeight")
    for edge in MST:
        print(f"{edge[0]}\t\t{edge[1]}")

main() 
    
    
