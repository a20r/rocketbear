
import graph


class DynamicSmallestDomainFirst(graph.ConstraintGraph):

    def ordering(self, v):
        return len(v.get_pruned_domain())


class StaticSmallestDomainFirst(graph.ConstraintGraph):

    def ordering(self, v):
        return len(v.get_full_domain())


class StaticMostArcsFirst(graph.ConstraintGraph):

    def ordering(self, v):
        return -len(self.edges[v])


class DynamicMostArcsFirst(graph.ConstraintGraph):

    def ordering(self, v):
        s = 0
        for nbr in self.edges[v]:
            if not nbr.is_assigned():
                s -= 1
        return s
