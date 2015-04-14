
import os
import sys

sys.path.append(os.path.join(os.path.dirname(__file__), ".."))

import time
import rocketbear

if __name__ == "__main__":
    g = rocketbear.GraphColouringInstance.load_col_file("graphs/myciel6.col")
    optimal_colouring = 7

    print "Dynamic Smallest Domain First:",
    start = time.time()
    sol = g.colour(optimal_colouring, rocketbear.DynamicSmallestDomainFirst)
    print time.time() - start

    print "Static Smallest Domain First:",
    start = time.time()
    sol = g.colour(optimal_colouring, rocketbear.StaticSmallestDomainFirst)
    print time.time() - start

    print "Static Most Arcs First:",
    start = time.time()
    sol = g.colour(optimal_colouring, rocketbear.StaticMostArcsFirst)
    print time.time() - start

    print "Dynamic Most Arcs First:",
    start = time.time()
    sol = g.colour(optimal_colouring, rocketbear.DynamicMostArcsFirst)
    print time.time() - start
