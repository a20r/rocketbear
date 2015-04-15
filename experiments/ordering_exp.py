
import os
import sys

sys.path.append(os.path.join(os.path.dirname(__file__), ".."))

import rocketbear


chromatic_numbers = {
    "graphs/queen5_5.col": 5,
    "graphs/queen6_6.col": 7,
    "graphs/queen7_7.col": 7,
    "graphs/jean.col": 10,
    "graphs/huck.col": 11,
    "graphs/myciel3.col": 4,
    "graphs/myciel4.col": 5,
    "graphs/myciel5.col": 6,
    "graphs/myciel6.col": 7,
    "graphs/myciel7.col": 8}


if __name__ == "__main__":
    #  Creates a rocketbear.GraphColouring instance from a file
    g = rocketbear.GraphColouringInstance.load_col_file(sys.argv[1])
    optimal_colouring = chromatic_numbers[sys.argv[1]]
    heuristic = rocketbear.orders[sys.argv[2]]

    sol = g.colour(optimal_colouring, heuristic)

    result = ",".join(map(str, [sys.argv[2],
                                optimal_colouring,
                                g.get_max_degree(),
                                g.get_avg_degree(),
                                g.get_number_of_edges(),
                                sol.get_time_taken(),
                                sol.get_num_assigned(),
                                sol.get_num_nodes(),
                                sol.get_num_backtracks()]))

    print result
