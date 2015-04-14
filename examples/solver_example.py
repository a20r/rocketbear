
import os
import sys

sys.path.append(os.path.join(os.path.dirname(__file__), ".."))

import rocketbear

"""
A toy example of the solver. The only correct response is:
    var_0 <- 2
    var_1 <- 3
    var_2 <- 4
"""


if __name__ == "__main__":
    # Initializes the variables and their domains
    var_0 = rocketbear.Variable([1, 2, 3, 4])
    var_1 = rocketbear.Variable([1, 2, 3, 4])
    var_2 = rocketbear.Variable([1, 2, 3, 4])

    # Unary constraints
    var_0.add_constraint(lambda x: x > 1)

    variables = [var_1, var_2, var_0]
    g = rocketbear.ConstraintGraph(variables)

    # Constraint function as a lambda function
    leq = lambda i, j: i <= j

    # Binary constraints
    g.add_constraint(var_0, var_1, leq)
    g.add_constraint(var_0, var_2, leq)
    g.add_constraint(var_1, var_2, leq)

    # Applies the all different constraint on all the variables
    g.all_different(*variables)

    # provides a solution to the constraint graph
    sol = g.solve()
    print sol
