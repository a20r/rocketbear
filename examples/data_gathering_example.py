
import os
import sys

sys.path.append(os.path.join(os.path.dirname(__file__), ".."))

import rocketbear

"""
An example of gathering statistics from different heuristics for a
given graph colouring instance.
"""

if __name__ == "__main__":
    #  Creates a rocketbear.GraphColouring instance from a file
    g = rocketbear.GraphColouringInstance.load_col_file("graphs/queen5_5.col")
    optimal_colouring = 5

    # Prints the legend
    print "Legend:"
    print "\tNA = Number of assignments"
    print "\tNN = Number of nodes"
    print "\tNB = Number of backtracks", "\n"

    sol = g.colour(optimal_colouring, rocketbear.DynamicSmallestDomainFirst)
    print "Heuristic: Dynamic Smallest Domain First"
    print "Time:", sol.get_time_taken()
    print "NA:", sol.get_num_assigned()
    print "NN:", sol.get_num_nodes()
    print "NB:", sol.get_num_backtracks(), "\n"

    sol = g.colour(optimal_colouring, rocketbear.StaticSmallestDomainFirst)
    print "Heuristic: Static Smallest Domain First"
    print "Time:", sol.get_time_taken()
    print "NA:", sol.get_num_assigned()
    print "NN:", sol.get_num_nodes()
    print "NB:", sol.get_num_backtracks(), "\n"

    sol = g.colour(optimal_colouring, rocketbear.StaticMostArcsFirst)
    print "Heuristic: Static Most Arcs First"
    print "Time:", sol.get_time_taken()
    print "NA:", sol.get_num_assigned()
    print "NN:", sol.get_num_nodes()
    print "NB:", sol.get_num_backtracks(), "\n"

    sol = g.colour(optimal_colouring, rocketbear.DynamicDomOverDeg)
    print "Heuristic: Dynamic Dom Over Deg"
    print "Time:", sol.get_time_taken()
    print "NA:", sol.get_num_assigned()
    print "NN:", sol.get_num_nodes()
    print "NB:", sol.get_num_backtracks(), "\n"

    sol = g.colour(optimal_colouring, rocketbear.DynamicMostArcsFirst)
    print "Heuristic: Dynamic Most Arcs First"
    print "Time:", sol.get_time_taken()
    print "NA:", sol.get_num_assigned()
    print "NN:", sol.get_num_nodes()
    print "NB:", sol.get_num_backtracks()
