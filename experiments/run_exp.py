
import os


chromatic_numbers = {
    "queen5_5.col": 5,
    "queen6_6.col": 7,
    "queen7_7.col": 7,
    "jean.col": 10,
    "huck.col": 11,
    "myciel3.col": 4,
    "myciel4.col": 5,
    "myciel5.col": 6,
    "myciel6.col": 7,
    "myciel7.col": 8}

heuristics = ["dsdf", "ssdf", "dmaf", "smaf", "ddod"]


if __name__ == "__main__":
    sys_cmd = "python experiments/ordering_exp.py graphs/{0} {1}\
        >> data/{0}.dat &"
    for gr in chromatic_numbers:
        for hr in heuristics:
            os.system(sys_cmd.format(gr, hr))
