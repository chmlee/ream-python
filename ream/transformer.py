"""
Transformer class
"""
import re
from lark import Transformer

class _Ream2Json(Transformer):
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
        return type(c)

    def com(self, c):
        return type(c)

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

class Ream2Json(Transformer):
    """
    something
    """

    def COMMENT(self, comment):
        return comment[2:] # strip leading "> "

    def STRING(self, string):
        return string[:]

    def NAME(self, name):
        return name[:]

    def KEY(self, key):
        return key[:-1] # strip trailing ":"
    

    def h_wrapper(self, wrapper):
        """
        wrapper[0]: entry name
        wrapper[1:]: content
        """
        name = wrapper[0]
        output_dict = {}
        for item in wrapper[1:]:
            # item[0]: key
            # item[1]: value
            # check value type
            key = item[0]
            value = item[1]
            val_type = type(value)
            if val_type != dict:
                output_dict[key] = value
            else: # dictionary !
                if key not in output_dict:
                    output_dict[key] = [value]
                else:
                    output_dict[key].append(value)
        return (name, output_dict)
    
    h1_wrapper = h_wrapper
    h2_wrapper = h_wrapper
    h3_wrapper = h_wrapper
    h4_wrapper = h_wrapper
    h5_wrapper = h_wrapper
    h6_wrapper = h_wrapper



    def start(self, everything):
        output_dict = {}
        for item in everything:
            # item[0]: key
            # item[1]: value
            # check value type
            key = item[0]
            value = item[1]
            val_type = type(value)
            if val_type != dict:
                output_dict[key] = value
            else: # dictionary !
                if key not in output_dict:
                    output_dict[key] = [value]
                else:
                    output_dict[key].append(value)
        return output_dict

    def value(self, val):
        """
        One of the following types:
            string_wrapper
            star_list
        """
        return val[0]

    def string_wrapper(self, wrapper):
        """
        wrapper[0]: STRING
        wrapper[1]: COMMENT (Optional)
        join the two as a string, separate by "__COM__"
        """
        try:
            string_output = "__COM__".join(wrapper)
        except IndexError:
            string_output = wrapper[0]
        return string_output

    def variable(self, var):
        """
        var[0]: KEY
        var[1]: value
        """
        return (var[0], var[1])

    def element(self, elem):
        try:
            string_output = "__COM__".join(elem)
        except IndexError:
            string_output = elem[0]
        return string_output

    def star_list(self, s_list):
        return s_list
