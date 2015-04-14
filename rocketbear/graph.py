
import arc
import solution
import copy
import time


class ConstraintGraph(object):

    def __init__(self, variables):
        self.arc_dict = dict()
        self.variables = variables
        self.variables_inds = list()
        self.edges = dict()

    def ordering(self, i):
        return self.variables.index(i)

    def add_constraint(self, i, j, constraint):
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
        neq = lambda a, b: a != b
        for ind, i in enumerate(vs):
            for j in vs[ind + 1:]:
                self.add_constraint(i, j, neq)

        return self

    def get_arc(self, i, j):
        return self.arc_dict[(i, j)]

    def has_arc(self, i, j):
        return (i, j) in self.arc_dict

    def get_best_variable(self):
        min_var = None
        min_val = None
        for i in self.variables_inds:
            val = self.ordering(self[i])
            if min_val is None or val < min_val:
                min_var = i
                min_val = val

        return min_var

    def setup_variable_inds(self):
        self.variables_inds = range(len(self.variables))
        return self

    def solve(self):
        n_graph = copy.deepcopy(self)
        n_graph.setup_variable_inds()
        res_graph = self.forward_checking(0, n_graph)
        if res_graph:
            sol = solution.Solution()
            for v in res_graph:
                sol[v.get_name()] = v.get_value()
            return sol
        else:
            return None

    def forward_checking(self, depth, graph):
        ind = graph.get_best_variable()
        for d in graph[ind].get_pruned_domain():
            if not graph[ind].check_constraints(d):
                continue

            last_graph = copy.deepcopy(graph)
            graph[ind].assign(d)
            consistent = True
            for future in graph.edges[graph[ind]]:
                vs = [future, graph[ind]]
                consistent = graph.get_arc(*vs).revise()
                if not consistent:
                    break

            if consistent:
                if depth == len(graph) - 1:
                    return graph
                else:
                    graph.variables_inds.remove(ind)
                    res = self.forward_checking(depth + 1, graph)
                    if res:
                        return res
            graph = last_graph

    def __getitem__(self, i):
        return self.variables[i]

    def __len__(self):
        return len(self.variables)

    def __str__(self):
        return "\n".join(str(v) for v in self.variables)
