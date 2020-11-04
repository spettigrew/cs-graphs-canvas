"""
Challenge
On your own, complete the following tasks:

Please spend a few minutes researching to find a unique use-case of a breadth-first-search.

Using the graph represented below, 
draw a picture of the graph and label each of the verts to show the correct vertex visitation order 
for a breadth-first-search starting with vertex "I".

Besides marking verts with colors as in the pseudo-code example, 
how else could you track the verts we have already visited?
"""

class Graph:
    def __init__(self):
        self.vertices = {
                            "A": {"B", "C", "D"},
                            "B": {},
                            "C": {"E", "F"},
                            "D": {"G"},
                            "E": {"G"},
                            "F": {"J"},
                            "G": {},
                            "H": {"C", "J", "K"},
                            "I": {"D", "E", "H"},
                            "J": {"L"},
                            "K": {"C"},
                            "L": {"M"},
                            "M": {},
                            "N": {"H", "K", "M"}
                        }


"""

Please spend a few minutes researching to find a unique use-case 
of a depth-first search.

Using the graph represented below, draw a picture of the graph and 
label each of the verts to show the correct vertex visitation order 
for a depth-first-search starting with vertex "I".
"""

# class Graph:
#     def __init__(self):
#         self.vertices = {
#                             "A": {"B", "C", "D"},
#                             "B": {},
#                             "C": {"E", "F"},
#                             "D": {"G"},
#                             "E": {"G"},
#                             "F": {"J"},
#                             "G": {},
#                             "H": {"C", "J", "K"},
#                             "I": {"D", "E", "H"},
#                             "J": {"L"},
#                             "K": {"C"},
#                             "L": {"M"},
#                             "M": {},
#                             "N": {"H", "K", "M"}
#                         }
