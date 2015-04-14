
import graph

"""
This file contains multiple heuristics that can be used for static and
dynamic variable orderings
"""

class DynamicSmallestDomainFirst(graph.ConstraintGraph):
    """
    Dynamic ordering where the variable with the currently smallest
    pruned domain is expanded frist
    """

    def ordering(self, v):
        """
        Returns the evaluation used for ordering for a node
        """
        return len(v.get_pruned_domain())


class StaticSmallestDomainFirst(graph.ConstraintGraph):
    """
    Static ordering where the variable with the overall smallest
    domain is expanded first
    """

    def ordering(self, v):
        """
        Returns the evaluation used for ordering for a node
        """
        return len(v.get_full_domain())


class StaticMostArcsFirst(graph.ConstraintGraph):
    """
    Static ordering where the variable with the overall largest number
    of constraints is expanded first
    """

    def ordering(self, v):
        """
        Returns the evaluation used for ordering for a node
        """
        return -len(self.edges[v])


class DynamicMostArcsFirst(graph.ConstraintGraph):
    """
    Dynamic ordering where the variable with the highest number of constraints
    to variables that are not already assigned is expanded first
    """

    def ordering(self, v):
        """
        Returns the evaluation used for ordering for a node
        """
        s = 0
        for nbr in self.edges[v]:
            if not nbr.is_assigned():
                s -= 1
        return s


#  Used for higher order functionality
orders = {
    "dsdf": DynamicSmallestDomainFirst,
    "ssdf": StaticSmallestDomainFirst,
    "smaf": StaticMostArcsFirst,
    "dmaf": DynamicMostArcsFirst
}
