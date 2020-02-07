from lark import Lark

with open('test1.md', 'r') as f:
    md = f.read()

print(md)


parser = Lark(r"""
        start: _NL? h1+

        h1: "#" h1_header _NL+ h1_content _NL*
        h1_header: /\w.*/
        h1_content: list_item*
        list_item: ["-"] /\w.*/ _NL+

        %import common.CNAME -> NAME
        %import common.NEWLINE -> _NL
        %import common.WS_INLINE

        %ignore WS_INLINE
    """, parser="lalr")



print('===============================================')
p = parser.parse(md)
#print(p)
#print(p.pretty())

from lark import Transformer, Tree
class test(Transformer):
    def list_item(self, content):
        (s,) = content
        return s[:]

    def h1_content(self, item_list):
        d = {}
        for item in item_list:
            string_list = item.split(":")
            d[string_list[0]] = string_list[1][1:]
        return d

    def h1_header(self, header):
        (header,) = header
        return header[:]

    def h1(self, entry):
        return entry

    def start(self, file):
        dict_of_dict = {}
        for entry in file:
            dict_name = entry[0]
            dict_item = entry[1]
            if dict_name not in dict_of_dict:
                dict_of_dict[dict_name] = [dict_item]
            else:
                dict_of_dict[dict_name].append(dict_item)
        return dict_of_dict


p = parser.parse(md)
output = test().transform(p)
print(output)
