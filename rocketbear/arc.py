
class Arc(object):

    def __init__(self, left, right):
        self.left = left
        self.right = right
        self.constraints = list()

    def add_constraint(self, constraint):
        self.constraints.append(constraint)
        return self

    def check_constraints(self, i, j):
        for constraint in self.constraints:
            if not constraint(i, j):
                return False
        return True

    def get_left(self):
        return self.left

    def get_right(self):
        return self.right

    def get_constraint(self):
        return self.constraint

    def revise(self):
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
