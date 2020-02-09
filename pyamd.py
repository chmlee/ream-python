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
        return h

    def v_list(self, v):
        return v

    def v_item(self, item):
        (item,) = item
        return item

    def na(self, n):
        ph = "NA" # may be customizable in the future
        return ph     

    def val(self, v):
        (v, ) = v
        return v

    def checkstring(self, x): # might rewrite with regex
        x_0 = x[0]
        if (x_0 == "'") or (x_0 == '"'):
            x = x[1:-1]
        else:
            try:
                x = int(x)
            except ValueError:
                try:
                    x = float(x)
                except ValueError:
                    pass
        return x



print('===============================================')

#with open('test1.md', 'r') as f:
#    md = f.read()
#p = parser.parse(md)
#output = test().transform(p)
#print(output)
#with open('test1.json', 'w') as fp:
#    json.dump(output, fp)

print('===============================================')

md1 = """
"""
p = parser.parse(md1)
print(p)
print('===============================================')
output = test().transform(p)
print(output)
with open('test.json', 'w') as fp:
    json.dump(output, fp)

print('===============================================')
