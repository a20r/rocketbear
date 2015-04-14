
import os
import sys

sys.path.append(os.path.join(os.path.dirname(__file__), ".."))

import rocketbear

"""
Simple example showing how variables are created with domains. Also
shows how the constraint graph can solve unary constraints
"""

if __name__ == "__main__":
    # Creates the variables
    var_0 = rocketbear.Variable([1, 2, 3, 4])
    var_1 = rocketbear.Variable([8, 9])

    # Adds unary constraints to the variables
    var_0.add_constraint(lambda i: i > 1)
    var_0.add_constraint(lambda i: i < 4)
    var_1.add_constraint(lambda i: i < 9)

    # Prints the variables
    print var_0
    print var_1

    cg = rocketbear.ConstraintGraph([var_0, var_1])
    sol = cg.solve()
    print sol
