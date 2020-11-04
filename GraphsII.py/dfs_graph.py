"""
Recursion
Since DFS will pursue leads in the graph as far as it can, and then "back up" to an earlier branch point to explore that way, recursion is an excellent approach to help "remember" where we left off.

Looking at it with pseudo-code to make the recursion more clear:

"""
# explore(graph) {
#     visit(this_vert);
#     explore(remaining_graph);
# }


"""
Pseudo-code for DFS
Let's explore some pseudo-code that shows a basic implementation 
of a depth-first-search of a graph.
"""
# two functions in our pseudo-code.
DFS(graph):
    # take the graph as the parameter
    for v of
     graph.verts:
    #  mark all the verts as unvisited.(white)
        v.color = white
        # Set the parent of each vert to null
        v.parent = null
    # this loop visits each vert in the graph
    for v of graph.verts:
        # if it's unvisited, it passes that vert into the second function.
        if v.color == white:
            DFS_visit(v)
#second function
DFS_visit(v):
    # marks the vert as gray (in the process of being explored)
    v.color = gray
    # then it loops through all of its unvisited neighbors.
    for neighbor of v.adjacent_nodes:
        if neighbor.color == white:
            # set the parent
            neighbor.parent = v
            # make a recursive call to the DFS_visit()
            DFS_visit(neighbor)
    # when done exploring all the neighbors, mark the vert as black (visited)
    v.color = black