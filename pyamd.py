from lark import Lark
import json


#print(md)



parser = Lark(r"""
        start: _NL? h1* dict*

        h1: "#"       name  _NL+  content1  _NL*
        h2: "##"      name  _NL+  content2  _NL*
        h3: "###"     name  _NL+  content3  _NL*
        h4: "####"    name  _NL+  content4  _NL*
        h5: "#####"   name  _NL+  content5  _NL*
        h6: "######"  name  _NL+  content6  _NL*

        content1: dict* h2*
        content2: dict* h3* 
        content3: dict* h4*
        content4: dict* h5*
        content5: dict* h6*
        content6: dict*
        
        item: dict

        dict: ("- "|"* ") key [val]  _NL+
        key: /.+:/
        val: /.+/

        name: /.+/

        %import common.CNAME -> NAME
        %import common.NEWLINE -> _NL
        %import common.WS_INLINE

        %ignore WS_INLINE
    """, parser="lalr")


print('===============================================')

from lark import Transformer, Tree

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

md1 = """
# something

- variable 1: 1
- variable 2: 2
- variable 3: -44
"""

p = parser.parse(md1)
output = test().transform(p)
print(output)
with open('test.json', 'w') as fp:
    json.dump(output, fp)

