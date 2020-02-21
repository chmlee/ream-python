"""
Transformer class
"""
import re
from lark import Transformer

class Ream2Json(Transformer):
    """
    something
    """

    def h(self, h):
        # remove comment
        h = [item for item in h if item is not None]
        ################
        return h
    h1 = h
    h2 = h
    h3 = h
    h4 = h
    h5 = h
    h6 = h
    h7 = h

    def name(self, n):
        (n,) = n
        n = n.strip()
        return n[:]

    def key(self, k):
        (k, ) = k
        k = k[:-1] #remove trailing :
        return k[:]


    def dict(self, d):
        # check if any value is stored
        tup = (d[0], d[1])
        return tup

    def item(self, i):
        return i

    def content(self, c):
        d = {}
        for item in c:
            key = item[0]
            val = item[1]
            # ignore comment
            if key == None:
                continue
            ################
            # store value
            if key not in d:
                d[key] = [val]
            else:
                d[key].append(val)
        # convert singleton of string to string
        for key in d:
            val = d[key]
            if len(val) == 1:
                d[key] = val[0]
        return d

    start = content
    content1 = content
    content2 = content
    content3 = content
    content4 = content
    content5 = content
    content6 = content

    # value config

    def string(self, s):
        (s,) = s
        s = str(s)
        if type(s) == str:
            s = self.checkstring(s)
        return s

    def h_list(self, h):
        (h,) = h
        return eval(h) # WARNING: SAFETY CONCERN!

    def v_list(self, v):
        return v

    def v_item(self, item):
        (item,) = item
        return item

    def na(self, n):
        return None

    def val(self, v):
        (v, ) = v
        return v

    def d_com(self, c):
        return (None, None)

    def h_com(self, c):
        return None

    def checkstring(self, x): # might rewrite with regex
        # check float
        if re.match(r"^-?[0-9]*\.[0-9]* *$", x):
            if x != ".": # "." is identified as float
                x_out = float(x)
            else:
                x_out = x
        # check integer
        elif re.match(r"^-?[0-9]* *$", x):
            x_out = int(x)
        # check whether number is forced to be stored as string
        elif re.match(r"^\'-?[0-9]*\.?[0-9]*\' *$", x) or re.match(r"^\"-?[0-9]*\.?[0-9]*\" *$", x):
            x_out = re.findall(r"-?[0-9]*\.?[0-9]*", x)[1]
        # binary response
        elif x == "TRUE":
            x_out = True
        elif x == "FALSE":
            x_out = False
        # no response
        elif x == "NA":
            x_out = None
        else:
            x_out = x
        return x_out