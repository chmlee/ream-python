from lark import Lark
import json

with open('test1.md', 'r') as f:
    md = f.read()

#print(md)



parser = Lark(r"""
        start: _NL? h1+

        h1: "#"       name  _NL+  content1  _NL*
        h2: "##"      name  _NL+  content2  _NL*
        h3: "###"     name  _NL+  content3  _NL*
        h4: "####"    name  _NL+  content4  _NL*
        h5: "#####"   name  _NL+  content5  _NL*
        h6: "######"  name  _NL+  content6  _NL*

        content1: item* h2*
        content2: list_item* h3* 
        content3: list_item* h4*
        content4: list_item* h5*
        content5: list_item* h6*
        content6: list_item*
        
        item: dict

        dict: "-" key val  _NL+
        key: /\w.*:/
        val: /\w.*/
           | item

        name: /\w.*/
        list_item: ["-"] /\w.*/ _NL+

        %import common.CNAME -> NAME
        %import common.NEWLINE -> _NL
        %import common.WS_INLINE

        %ignore WS_INLINE
    """, parser="lalr")


print('===============================================')
p = parser.parse(md)
print(p.pretty())
#print(p)
#print(p.pretty())

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
        return (d[0], d[1])

    def item(self, i):
        return i[0]
    

    def content(self, c):
        d = {}
        for item in c:
            key = item[0]
            val = item[1]
            if key not in d:
                d[key] = [val]
            else:
                d[key].append(val)
        # convert singleton of string to string
        for key in d:
            val = d[key]
            if len(val) == 1:
                if type(val[0]) == str:
                    d[key] = val[0]
        return d

    start = content
    content1 = content
    


    def h1(self, h):
        return h


print('===============================================')
p = parser.parse(md)
output = test().transform(p)
print(output)


