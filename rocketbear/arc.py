
class Arc(object):
    """
    Python representation of a constraint arc
    """

    def __init__(self, left, right):
        """
        Since the arc is a directed edge, the left and right components
        of the arc are initalized where the arc travels from left to right.
        """
        self.left = left
        self.right = right
        self.constraints = list()

    def add_constraint(self, constraint):
        """
        Adds a constraint to the arc. The constraint is a function that
        takes two node values and returns a boolean result
        """
        self.constraints.append(constraint)
        return self

    def check_constraints(self, i, j):
        """
        Returns true if the all of the constraints are satisfied for
        i and j being node values not variable instances
        """
        for constraint in self.constraints:
            if not constraint(i, j):
                return False
        return True

    def get_left(self):
        """
        Gets the left side of the arc
        """
        return self.left

    def get_right(self):
        """
        Gets the right side of the arc
        """
        return self.right

    def get_constraints(self):
        """
        Gets the list of constraints
        """
        return self.constraints

    def revise(self):
        """
        Revises the arc where the right variable has already been assigned
        a value, this function prunes the domain of the left variable to
        keep consistency. Returns true if there is a consistent pruned domain
        for the left variable.
        """
        pd = list()
        for d in self.left.get_pruned_domain():
            unary_check = self.left.check_constraints(d)
            arc_check = self.check_constraints(d, self.right.get_value())
            if unary_check and arc_check:
                pd.append(d)

        if len(pd) > 0:
            self.left.set_pruned_domain(pd)
            return True
        else:
            return False
