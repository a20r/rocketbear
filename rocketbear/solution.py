
class Solution(dict):
    """
    A Python representation of a solution for a constraint graph.
    This extends a dictionary to hold custom values as well as
    a more suitable string method.
    """

    def __str__(self):
        """
        Converts the solution into a string that can be printed
        """
        assigns = "\n\t".join("{} = {}".format(key, self[key])
                         for key in self.keys())
        return "Assignments:\n\t{}".format(assigns)

    def set_time_taken(self, tt):
        """
        Sets the time the experiment has taken
        """
        self.tt = tt
        return self

    def set_num_assigned(self, na):
        """
        Sets the number of assignments used in the search. This is for
        data gathering purposes
        """
        self.na = na
        return self

    def set_num_nodes(self, nn):
        """
        Sets the number of nodes used in the search. This is for data
        gathering and analyssi purposes
        """
        self.nn = nn
        return self

    def set_num_backtracks(self, nb):
        """
        Sets the number of backtracks used in the search. This is for data
        gathering and analysis purposes
        """
        self.nb = nb
        return self

    def get_time_taken(self):
        """
        Gets the time the experiment took
        """
        return self.tt

    def get_num_assigned(self):
        """
        Gets the number of assignments used for the search
        """
        return self.na

    def get_num_nodes(self):
        """
        Gets the number of nodes used in the search
        """
        return self.nn

    def get_num_backtracks(self):
        """
        Gets the number of backtracks used in the search
        """
        return self.nb
