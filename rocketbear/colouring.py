
import variable


class GraphColouringInstance(object):
    """
    Graph colouring problem instance that can be used
    to find the chromatic number of a graph using a constraint
    graph
    """

    def __init__(self):
        """
        Initializes the nodes and edges. This class is basically
        just a simple representation of a graph that also incorporates
        determining the chromatic number
        """
        self.nodes = set()
        self.edges = dict()

    def degree(self, i):
        """
        Gets the degree for a node
        """
        if self.has_node(i):
            return len(self.edges[i])
        else:
            return 0

    def add_edge(self, i, j):
        """
        Adds an edge between node value i to node value j
        """
        self.nodes.add(i)
        self.nodes.add(j)

        if not i in self.edges:
            self.edges[i] = set()

        if not j in self.edges:
            self.edges[j] = set()

        self.edges[i].add(j)
        self.edges[j].add(i)
        return self

    def has_edge(self, i, j):
        """
        Returns true if there is an edge between node value i
        and node value j
        """
        return i in self.edges and j in self.edges[i]

    def has_node(self, i):
        """
        Returns true if the node value i is in the graph
        """
        return i in self.nodes

    def get_constraint_graph(self, max_colouring, heuristic):
        """
        Converts the graph colouring problem instance into a constraint
        graph by setting binary constraints between nodes in the graph
        such that they cannot be the same color. Also sets unary
        constraints on each node specifying that their value cannot
        be greater than the maximum colors used in the search.
        This function also takes in a heuristic that is just a child class
        of ConstraintGraph which has a custom ordering function
        """
        vs = list()
        var_dict = dict()
        for i in self.nodes:
            v = variable.Variable(range(max_colouring), name=i)
            v.add_constraint(lambda x: x < max_colouring)
            var_dict[i] = v
            vs.append(v)

        neq = lambda a, b: a != b
        cg = heuristic(vs)
        for i in self.nodes:
            for j in self.edges[i]:
                cg.add_constraint(var_dict[i], var_dict[j], neq)

        return cg

    def colour(self, max_colouring, heuristic):
        """
        Colours the graph using a heuristic variable ordering and a
        maximum colouring
        """
        cg = self.get_constraint_graph(max_colouring, heuristic)
        return cg.solve()

    @staticmethod
    def load_col_file(filename):
        """
        Loads a graph from a file using the standard DIMACS format
        """
        gci = GraphColouringInstance()
        with open(filename) as f:
            text = f.read()
            lines = text.split("\n")
            for line in lines:
                lstr = line.strip()
                if lstr.startswith("e"):
                    cols = lstr.split(" ")
                    i = int(cols[1])
                    j = int(cols[2])
                    gci.add_edge(i, j)

            return gci
