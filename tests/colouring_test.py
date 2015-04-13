
import os
import sys

sys.path.append(os.path.join(os.path.dirname(__file__), ".."))

import rocketbear

if __name__ == "__main__":
    g = rocketbear.GraphColouringInstance\
        .load_col_file("graphs/queen5_5.col")
    sol = g.colour(5)
    print sol
