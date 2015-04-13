
import variable
import graph


class GraphColouringInstance(object):

    def __init__(self):
        self.nodes = set()
        self.edges = dict()

    def degree(self, i):
        if self.has_node(i):
            return len(self.edges[i])
        else:
            return 0

    def add_edge(self, i, j):
        self.nodes.add(i)
        self.nodes.add(j)

        if not i in self.edges:
            self.edges[i] = set()

        if not j in self.edges:
            self.edges[j] = set()

        self.edges[i].add(j)
        self.edges[j].add(i)

    def has_edge(self, i, j):
        return i in self.edges and j in self.edges[i]

    def has_node(self, i):
        return i in self.nodes

    def get_constraint_graph(self, max_colouring):
        vs = list()
        var_dict = dict()
        for i in self.nodes:
            v = variable.Variable(range(self.degree(i) + 1), name=i)
            v.add_constraint(lambda x: x < max_colouring)
            var_dict[i] = v
            vs.append(v)

        neq = lambda a, b: a != b
        cg = graph.ConstraintGraph(vs, ordering="accending_domain")
        for i in self.nodes:
            for j in self.edges[i]:
                cg.add_constraint(var_dict[i], var_dict[j], neq)

        return cg

    def colour(self, max_colouring):
        cg = self.get_constraint_graph(max_colouring)
        return cg.solve()

    @staticmethod
    def load_col_file(filename):
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
