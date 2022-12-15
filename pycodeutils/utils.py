from parse import findall

from .core import list

def extract_ints(string):
    return list(value[0] for value in findall("{:d}", string)).mapped(lambda x: int(x))

def xrange(start, end):
    step = 1 if end >= start else -1
    return range(start, end + step, step)