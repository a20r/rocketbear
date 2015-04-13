
import os
import sys

sys.path.append(os.path.join(os.path.dirname(__file__), ".."))

import rocketbear

if __name__ == "__main__":
    var_0 = rocketbear.Variable([1, 2, 3, 4])
    var_1 = rocketbear.Variable([1, 2, 3, 4])
    var_2 = rocketbear.Variable([1, 2, 3, 4])

    # Unary constraints
    var_0.add_constraint(lambda x: x > 1)

    variables = [var_1, var_2, var_0]
    g = rocketbear.ConstraintGraph(variables, ordering="accending_domain")

    # Binary constraints
    g.add_constraint(var_0, var_1, lambda i, j: i <= j)
    g.add_constraint(var_0, var_2, lambda i, j: i <= j)
    g.add_constraint(var_1, var_2, lambda i, j: i <= j)
    g.all_different(*variables)
    sol = g.solve()
    print sol
