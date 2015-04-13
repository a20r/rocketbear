
import os
import sys

sys.path.append(os.path.join(os.path.dirname(__file__), ".."))

import rocketbear

if __name__ == "__main__":
    var_0 = rocketbear.Variable([1, 2, 3, 4])
    var_1 = rocketbear.Variable([1, 2, 3, 4])
    print var_0
    print var_1
