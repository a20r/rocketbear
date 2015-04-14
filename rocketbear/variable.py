

class Variable(object):
    """
    Python representation of a variable. This variable may be assigned
    and contains both a pruned and pure domain. The variable class also
    contains all of the unary constraints that are imposed on the variable
    itself.
    """

    #  The number of anon variables that have been instatiated
    NUM_VARS = 0

    def __init__(self, domain, name=None):
        """
        Initializes the variable with a given domain and name. The
        pruned domain starts off as the pure full domain
        """
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
        """
        Check if all the unary constraints hold for a assignment v
        """
        for constraint in self.constraints:
            if not constraint(v):
                return False
        return True

    def add_constraint(self, constraint):
        """
        Adds a unary constraint on the variable. The constraint takes in
        one node value and returns a boolean variable
        """
        self.constraints.append(constraint)
        return self

    def get_name(self):
        """
        Gets the name of the variable
        """
        return self.name

    def get_domain_size(self):
        """
        Gets the size of the full variable domain
        """
        return len(self.domain)

    def get_full_domain(self):
        """
        Returns the full unpruned domain
        """
        return self.domain

    def get_pruned_domain(self):
        """
        Gets the pruned domain
        """
        return self.pruned_domain

    def get_value(self):
        """
        Gets the assigned value of the variable. This may be None
        if the variable has not yet been assigned
        """
        return self.value

    def set_pruned_domain(self, pd):
        """
        This sets the pruned domain to pd
        """
        self.pruned_domain = pd
        return self

    def is_assigned(self):
        """
        Checks if the variable is assigned or not
        """
        return not self.value is None

    def assign(self, v):
        """
        Assigns the value of the variable to v
        """
        self.value = v
        return self

    def __eq__(self, other):
        """
        Overwrites the = operator
        """
        return self.name == other.name

    def __hash__(self):
        """
        Hashs the variable based on its name
        """
        return hash(self.name)

    def __str__(self):
        """
        Returns a string represenation of a variable
        """
        nm = "Variable: {}".format(self.name)
        val = "Value: {}".format(self.value)
        dom = "Domain: {}".format(self.domain)
        p_dom = "Pruned Domain: {}".format(self.pruned_domain)
        return "{}\n\t{}\n\t{}\n\t{}".format(nm, val, dom, p_dom)
