
import arc
import solution
import copy
import time


class ConstraintGraph(object):
    """
    Python representation of a constraint graph
    """

    def __init__(self, variables):
        """
        Given a list of variables with unary constraints,
        this generates a constraint graph with no binary
        constraints. The binary constraints are added later
        """
        self.arc_dict = dict()
        self.variables = variables
        self.variables_inds = list()
        self.edges = dict()
        self.num_assigned = 0
        self.num_nodes = 0
        self.num_backtracks = 0

    def ordering(self, i):
        """
        This function should be overridden by other heuristics.
        The current heuristic is the static variable ordering
        """
        return self.variables.index(i)

    def add_constraint(self, i, j, constraint):
        """
        Adds a constraint between two variables in the constraint graph.
        The constraint is a function that takes in two values and returns
        a boolean result
        """
        if not self.has_arc(i, j):
            self.arc_dict[(i, j)] = arc.Arc(i, j)
            self.arc_dict[(j, i)] = arc.Arc(j, i)

        if not i in self.edges:
            self.edges[i] = set()

        if not j in self.edges:
            self.edges[j] = set()

        inv_c = lambda a, b: constraint(b, a)
        self.arc_dict[(i, j)].add_constraint(constraint)
        self.arc_dict[(j, i)].add_constraint(inv_c)
        self.edges[i].add(j)
        self.edges[j].add(i)
        return self

    def all_different(self, *vs):
        """
        Applies the AllDifferent constraint for a group of variables
        in the constraint graph
        """
        neq = lambda a, b: a != b
        for ind, i in enumerate(vs):
            for j in vs[ind + 1:]:
                self.add_constraint(i, j, neq)

        return self

    def get_arc(self, i, j):
        """
        Gets the arc representation between two variables
        """
        return self.arc_dict[(i, j)]

    def has_arc(self, i, j):
        """
        Check if there is an arc between two variables
        """
        return (i, j) in self.arc_dict

    def get_best_variable(self):
        """
        Finds the current variable that has not been assigned that
        has the minimal value for the ordering function. This determines
        the order in which variables are searched
        """
        min_var = None
        min_val = None
        for i in self.variables_inds:
            val = self.ordering(self[i])
            if min_val is None or val < min_val:
                min_var = i
                min_val = val

        return min_var

    def setup_variable_inds(self):
        """
        Initializes the variable index for search
        """
        self.variables_inds = range(len(self.variables))
        return self

    def solve(self):
        """
        Provides a solution to the constraint graph using forward
        checking
        """
        n_graph = copy.deepcopy(self)
        n_graph.setup_variable_inds()
        start = time.time()
        res_graph = self.forward_checking(0, n_graph)
        end = time.time() - start
        if res_graph:
            sol = solution.Solution()
            for v in res_graph:
                sol[v.get_name()] = v.get_value()
            sol.set_num_assigned(self.num_assigned)
            sol.set_num_nodes(self.num_nodes)
            sol.set_num_backtracks(self.num_backtracks)
            sol.set_time_taken(end)
            self.num_assigned = 0
            self.num_nodes = 0
            self.num_backtracks = 0
            return sol
        else:
            return None

    def forward_checking(self, depth, graph):
        """
        Recursive function to perform forward checking. Variables
        are ordered based on the ordering function that may be overridden
        """
        ind = graph.get_best_variable()
        self.num_nodes += 1
        for d in graph[ind].get_pruned_domain():
            if not graph[ind].check_constraints(d):
                continue

            last_graph = copy.deepcopy(graph)
            graph[ind].assign(d)
            self.num_assigned += 1

            # Finally I get to use a for-else statement :D
            for future in graph.edges.get(graph[ind], list()):
                vs = [future, graph[ind]]
                if not graph.get_arc(*vs).revise():
                    break
            else:
                if depth == len(graph) - 1:
                    return graph
                else:
                    graph.variables_inds.remove(ind)
                    res = self.forward_checking(depth + 1, graph)
                    if res:
                        return res
            self.num_backtracks += 1
            graph = last_graph

    def __getitem__(self, i):
        """
        Operator overloading for indexing. We can now index the graph
        based on the the index of the variables in the variable list
        """
        return self.variables[i]

    def __len__(self):
        """
        Gets the number of variables in the graph
        """
        return len(self.variables)

    def __str__(self):
        """
        Returns a string representatino of the graph
        """
        return "\n".join(str(v) for v in self.variables)
