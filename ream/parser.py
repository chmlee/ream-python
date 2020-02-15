"""
Parser
"""
from lark import Lark

REAM_RULE = Lark(r"""
    start: _NL? dict* h1*

    h1: "#"       name  _NL*  [ h_com _NL* ] content1  _NL*
    h2: "##"      name  _NL*  [ h_com _NL* ] content2  _NL*
    h3: "###"     name  _NL*  [ h_com _NL* ] content3  _NL*
    h4: "####"    name  _NL*  [ h_com _NL* ] content4  _NL*
    h5: "#####"   name  _NL*  [ h_com _NL* ] content5  _NL*
    h6: "######"  name  _NL*  [ h_com _NL* ] content6  _NL*

    name: /.+/

    content1: (dict [d_com])* h2*
    content2: (dict [d_com])* h3* 
    content3: (dict [d_com])* h4*
    content4: (dict [d_com])* h5*
    content5: (dict [d_com])* h6*
    content6: (dict [d_com])*

    item: dict

    dict: "- " key val _NL*
    key: /.+:/
    val: na
       | h_list
       | string
       | v_list

    string: /.+/

    v_list: _NL ( "* " v_item _NL)+
    v_item: val

    na: _NL


    h_list:  /\[.+\]/

    d_com: /(>.*\n)+/
    h_com: /(>.*\n)+/


    %import common.CNAME -> NAME
    %import common.NEWLINE -> _NL
    %import common.WS_INLINE

    %ignore WS_INLINE
""",
parser="lalr")
