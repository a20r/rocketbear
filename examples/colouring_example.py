
import os
import sys

sys.path.append(os.path.join(os.path.dirname(__file__), ".."))

import rocketbear

"""
An example of graph colouring using the DynamicSmallestDomainFirst
heuristic from the orderings file
"""

if __name__ == "__main__":
    #  Creates a rocketbear.GraphColouring instance from a file
    g = rocketbear.GraphColouringInstance.load_col_file("graphs/huck.col")
    print sum(len(g.edges[i]) for i in g.edges) / 2
    optimal_colouring = 11

    sol = g.colour(optimal_colouring, rocketbear.DynamicSmallestDomainFirst)
    print "Chromatic number:", optimal_colouring
    print sol
