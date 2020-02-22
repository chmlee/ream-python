"""
Transformer class
"""
import re
import yaml
from lark import Transformer

class Ream2Json(Transformer):
    """
    something
    """


    def meta_wrapper(self, wrapper):
        output_dict = yaml.safe_load("".join([f"{x}\r" for x in wrapper]))
        return ["__metadata__", output_dict]

    def META(self, meta):
        return meta

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
