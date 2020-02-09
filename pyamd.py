from lark import Lark, Transformer, Tree
import json
import ast

with open("parser_rule.yaml", "r") as f:
    prule = f.read()

parser = Lark(prule, parser="lalr")

class test(Transformer):
    
    def h(self, h):
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

    def val(self, v):
        (v, ) = v
        return v[:]

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
            # convert value to integer if possible
            # NOTE: try except might be too costly
            if type(val) == str:
                try:
                    val = int(val)
                except ValueError:
                    try:
                        val = float(val)
                    except ValueError:
                        pass
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

    def str_int(self, s):
        (s,) = s
        return s

    def h_list(self, h):
        (h,) = h
        if h[0] == "[":
            try:
                h = ast.literal_eval(h)
            except (ValueError, SyntaxError):
                pass
        return h

    def na(self, n):
        ph = "NA" # may be customizable in the future
        return ph     




print('===============================================')

with open('test1.md', 'r') as f:
    md = f.read()
p = parser.parse(md)
output = test().transform(p)
print(output)
with open('test1.json', 'w') as fp:
    json.dump(output, fp)

print('===============================================')

md1 = """
- variable 1: [1, 2, 3]
- variable 2: 
"""
p = parser.parse(md1)
print(p)
print('===============================================')
output = test().transform(p)
print(output)
with open('test.json', 'w') as fp:
    json.dump(output, fp)

print('===============================================')
