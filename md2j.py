from lark import Lark

with open('test1.md', 'r') as f:
    md = f.read()

print(md)


parser = Lark(r"""
        start: _NL? h1+

        h1: h1_header _NL+ h1_content _NL*
        h1_header: "#" /\w.*/
        h1_content: list_item* h2*

        h2: h2_header _NL+ h2_content _NL*
        h2_header: "##" /\w.*/
        h2_content: list_item*  

        list_item: ["-"] /\w.*/ _NL+

        %import common.CNAME -> NAME
        %import common.NEWLINE -> _NL
        %import common.WS_INLINE

        %ignore WS_INLINE
    """, parser="lalr")


parser = Lark(r"""
        start: _NL? h1+

        h1: "#"       name  _NL+  content1  _NL*
        h2: "##"      name  _NL+  content2  _NL*
        h3: "###"     name  _NL+  content3  _NL*
        h4: "####"    name  _NL+  content4  _NL*
        h5: "#####"   name  _NL+  content5  _NL*
        h6: "######"  name  _NL+  content6  _NL*

        content1: list_item* h2*
        content2: list_item* h3* 
        content3: list_item* h4*
        content4: list_item* h5*
        content5: list_item* h6*
        content6: list_item*

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

    #def start(self, file):
    #    dict_of_dict = {}
    #    for entry in file:
    #        dict_name = entry[0]
    #        dict_item = entry[1]
    #        if dict_name not in dict_of_dict:
    #            dict_of_dict[dict_name] = [dict_item]
    #        else:
    #            dict_of_dict[dict_name].append(dict_item)
    #    return dict_of_dict
    #content2 = start

     



p = parser.parse(md)
output = test().transform(p)
print(output)
print('===============================================')

Tree(
    start, [
        Tree(
            h1, 
            [
                'Group Level Meta-Data', 
                Tree(content1, 
                    [
                        ['key 1', 'value 1'], 
                        ['key 2', 'value 2'], 
                        Tree(h2, 
                            [
                                'Level 2', 
                                Tree(content2, 
                                    [
                                        ['AAA', 'aaa'], 
                                        ['BBB', 'bbb']
                                    ]
                                )
                            ]
                        ), 
                        Tree(h2, 
                            [
                                'Level 2', 
                                Tree(content2, 
                                    [
                                        ['CCC', 'ccc'], 
                                        ['DDD', 'ddd'], 
                                        Tree(h3, 
                                            [
                                                'Level 3', 
                                                Tree(content3, 
                                                    [
                                                        ['123', '456'], 
                                                        ['789', '000']
                                                    ]
                                                ),
                                            ]
                                        ),
                                        Tree(h3, 
                                            [
                                                'Level 3', 
                                                Tree(content3, 
                                                    [
                                                        ['123', '456'], 
                                                        ['789', '000']
                                                    ]
                                                ),
                                            ]
                                        )
                                    ]
                                )
                            ]
                        )
                    ]
                )
            ]
        ), 
    Tree(h1, ['Group Level Meta-Data', Tree(content1, [['key 1', 'value 1'], ['key 2', 'value 2']])])])

