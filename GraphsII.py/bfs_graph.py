"""
Pseudo-code for BFS - breadth first search
Pseudo-code that shows a basic implementation of a breadth-first-search of a graph.

"""

BFS(graph, startVert):
    # set up a graph with vertices
    for v of graph.vertexes:
        # go through each of the vertices in the graph and mark them with the color white.
        # At the outset, we mark all the verts as unvisited.
        v.color = white
    #mark  starting vert as gray. We are exploring the starting verts neighbors.
    startVert.color = gray
        # We enqueue the starting vert, the first vert we look at once we enter the while loop
        queue.enqueue(startVert)
    # if queuue is not empty, we peek at the first item in the queue by storing it in a varialble.
    while !queue.isEmpty():
        u = queue[0]  # Peek at head of the queue, but do not dequeue!
        # loop through each of the verts neighbors and we check if it's unvisited.
        for v of u.neighbors:
            if v.color == white:
                #if it's unvisited we mark it as gray.
                v.color = gray
                # then we enqueue the vert
                queue.enqueue(v)
        # we dequeue the current vert we've been exploring and mark that vert as black
        queue.dequeue()
        u.color = black


