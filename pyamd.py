from lark import Lark, Transformer, Tree
import json

with open("parser_rule", "r") as f:
    prule = f.read()

parser = Lark(prule, parser="lalr")

class test(Transformer):
    
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
        if len(d) == 2:
            tup = (d[0], d[1])
        else:
            tup = (d[0], "NA") # future version may allow user to customize no response
        return tup

    def item(self, i):
        return i
    

    def content(self, c):
        d = {}
        for item in c:
            key = item[0]
            val = item[1]
            try:
                val = int(val)
            except ValueError:
                pass
            except TypeError:
                pass
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
    


    def h(self, h):
        return h
    h1 = h
    h2 = h
    h3 = h
    h4 = h
    h5 = h
    h6 = h
    h7 = h


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
- variable 1:value 1
 * variable 2: 2
     -       variable   3   :   3.14
"""
p = parser.parse(md1)
output = test().transform(p)
print(output)
with open('test.json', 'w') as fp:
    json.dump(output, fp)

print('===============================================')
