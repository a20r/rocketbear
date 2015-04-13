
class Solution(dict):

    def __str__(self):
        return "\n".join("{} = {}".format(key, self[key])
                         for key in self.keys())
