

class Variable(object):

    NUM_VARS = 0

    def __init__(self, domain, name=None):
        self.domain = domain
        self.pruned_domain = domain
        self.value = None
        if name:
            self.name = str(name)
        else:
            self.name = "x{}".format(Variable.NUM_VARS)
            Variable.NUM_VARS += 1

        self.constraints = list()

    def check_constraints(self, v):
        for constraint in self.constraints:
            if not constraint(v):
                return False
        return True

    def add_constraint(self, constraint):
        self.constraints.append(constraint)
        return self

    def get_name(self):
        return self.name

    def get_domain_size(self):
        return len(self.domain)

    def get_full_domain(self):
        return self.domain

    def get_pruned_domain(self):
        return self.pruned_domain

    def get_value(self):
        return self.value

    def set_pruned_domain(self, pd):
        self.pruned_domain = pd
        return self

    def is_assigned(self):
        return not self.value is None

    def assign(self, v):
        self.value = v
        return self

    def __eq__(self, other):
        return self.name == other.name

    def __hash__(self):
        return hash(self.name)

    def __str__(self):
        nm = "Variable: {}".format(self.name)
        val = "Value: {}".format(self.value)
        dom = "Domain: {}".format(self.domain)
        p_dom = "Pruned Domain: {}".format(self.pruned_domain)
        return "{}\n\t{}\n\t{}\n\t{}".format(nm, val, dom, p_dom)
