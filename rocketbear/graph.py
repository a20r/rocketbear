
import arc
import solution
import copy


class ConstraintGraph(object):

    def __init__(self, variables, ordering=None):
        self.arc_dict = dict()
        self.variables = self.init_variables(variables, ordering)

    def init_variables(self, variables, ordering):
        if ordering == "accending_domain":
            domain_ordering = lambda v: v.get_domain_size()
            vs = sorted(variables, key=domain_ordering)
        else:
            vs = variables

        return vs

    def add_constraint(self, i, j, constraint):
        if not self.has_arc(i, j):
            self.arc_dict[(i, j)] = arc.Arc(i, j)
            self.arc_dict[(j, i)] = arc.Arc(j, i)

        inv_c = lambda a, b: constraint(b, a)
        self.arc_dict[(i, j)].add_constraint(constraint)
        self.arc_dict[(j, i)].add_constraint(inv_c)
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
        return self.arc_dict.has_key((i, j))

    def solve(self):
        n_graph = copy.deepcopy(self)
        res_graph = self.__forward_checking(0, n_graph)
        if res_graph:
            sol = solution.Solution()
            for v in res_graph:
                sol[v.get_name()] = v.get_value()
            return sol
        else:
            return None

    def __forward_checking(self, depth, graph):
        for d in graph[depth].get_pruned_domain():
            if not graph[depth].check_constraints(d):
                continue

            last_graph = copy.deepcopy(graph)
            graph[depth].assign(d)
            consistent = True
            for future in xrange(depth + 1, len(graph)):
                if graph.has_arc(graph[future], graph[depth]):
                    vs = [graph[future], graph[depth]]
                    consistent = graph.get_arc(*vs).revise()
                if not consistent:
                    break

            if consistent:
                if depth == len(graph) - 1:
                    return graph
                else:
                    res = self.__forward_checking(depth + 1, graph)
                    if res:
                        return res
                    else:
                        graph = last_graph
            else:
                graph = last_graph

    def __getitem__(self, i):
        return self.variables[i]

    def __len__(self):
        return len(self.variables)

    def __str__(self):
        return "\n".join(str(v) for v in self.variables)
