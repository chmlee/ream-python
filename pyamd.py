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
        return n[:]

    def key(self, k):
        (k, ) = k
        return k[:-1]

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


p = parser.parse(md)
output = test().transform(p)
print(output)

print('===============================================')

class convert(Transformer):

    def list_item(self, item):
        (item_string, ) = item
        item_string_list = item_string.split(": ")
        l = [item_string_list[0], item_string_list[1]]
        return l

    def name(self, n):
        (n, ) = n
        return n[:]


    def content(self, input):
        d = {}
        pair_list = input[:]
        for pair in pair_list:
            key = pair[0]
            val = pair[1]
            if key not in d:
                d[key] = [val]
            else:
                d[key].append(val)
        # unlist string
        for key in d:
            first_item = d[key][0] 
            if type(first_item) != dict:
                d[key] = first_item
        return d
    content1 = content
    content2 = content
    content3 = content
    content4 = content
    content5 = content
    content6 = content
    start = content
    
    def h(self, stuff):
        return stuff[:]
    h1 = h
    h2 = h
    h3 = h
    h4 = h
    h5 = h
    h6 = h




#p = parser.parse(md)
#output = convert().transform(p)
#print('===============================================')
#
#
#print(json.dumps(output, indent =4))



