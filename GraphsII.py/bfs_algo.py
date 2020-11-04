class Vertex:
    def __init__(self, value):
        self.value = value
        self.connections = {}

    def __str__(self):
        return str(self.value) + ' connections: ' + str([x.value for x in self.connections])

    def add_connection(self, vert, weight = 0):
        self.connections[vert] = weight

    def get_connections(self):
        return self.connections.keys()

    def get_value(self):
        return self.value

    def get_weight(self, vert):
        return self.connections[vert]

# class Graph:
#     def __init__(self):
#         self.vertices = {}
#         self.count = 0

#     def __contains__(self, vert):
#         return vert in self.vertices

#     def __iter__(self):
#         return iter(self.vertices.values())

#     def add_vertex(self, value):
#         self.count += 1
#         new_vert = Vertex(value)
#         self.vertices[value] = new_vert
#         return new_vert

#     def add_edge(self, v1, v2, weight = 0):
#         if v1 not in self.vertices:
#             self.add_vertex(v1)
#         if v2 not in self.vertices:
#             self.add_vertex(v2)
#         self.vertices[v1].add_connection(self.vertices[v2], weight)

#     def get_vertices(self):
#         return self.vertices.keys()


# Now, we will add a breadth_first_search method to our Graph class. 
# One of the most common and simplest ways to implement a BFS is to use a queue 
# to keep track of unvisited nodes and a set to keep track of visited nodes. 
# Let's start by defining the start of our function with these structures:

class Graph:
    def __init__(self):
        self.vertices = {}
        self.count = 0

    def __contains__(self, vert):
        return vert in self.vertices

    def __iter__(self):
        return iter(self.vertices.values())

    def add_vertex(self, value):
        self.count += 1
        new_vert = Vertex(value)
        self.vertices[value] = new_vert
        return new_vert

    def add_edge(self, v1, v2, weight = 0):
        if v1 not in self.vertices:
            self.add_vertex(v1)
        if v2 not in self.vertices:
            self.add_vertex(v2)
        self.vertices[v1].add_connection(self.vertices[v2], weight)

    def get_vertices(self):
        return self.vertices.keys()

    # in a BFS, we use a queue to keep track of all the things we need to visit
    def breadth_first_search(self, starting_vert):
        # store to_vist, and use a queue to store all the vertices we need to vist.
        to_visit = Queue()
        # Keep track of all the vertices that we have visited O(1) - constant time
        visited = set()
        # enqueue the starting vertex to visit,
        # because that's the first vertex we need to visit
        to_visit.enqueue(starting_vert)
        # we now add the starting vert to our visited
        visited.add(starting_vert)
        # go through every level in the graph, until there is nothing left to visit, then we're done.
        while to_visit.size() > 0:
            # we dequeue the val.ue in the queue and check all of it's neighbors level by level
            current_vert = to_visit.dequeue()
            # check all of the current verts neighbors
            for next_vert in current_vert.get_connections():
                # check to see if we've already visited
                if next_vert not in visited:
                    # if not visited, we will visit it
                    visited.add(next_vert)
                    # enqueue next vert onto our que visit. 
                    to_visit.enqueue(next_vert)
