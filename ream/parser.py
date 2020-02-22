"""
Parser
"""
from lark import Lark

REAM_RULE = Lark(r"""
    start: _NL? variable* h1_wrapper*
    
    _DASH:     "- "
    _STAR:     "*"
    _HEADER_1: "#"
    _HEADER_2: "##"
    _HEADER_3: "###"
    _HEADER_4: "####"
    _HEADER_5: "#####"
    _HEADER_6: "######"

    NAME: /.+/

    h1_wrapper: _HEADER_1 NAME _NL* variable* h2_wrapper*
    h2_wrapper: _HEADER_2 NAME _NL* variable* h3_wrapper*
    h3_wrapper: _HEADER_3 NAME _NL* variable* h4_wrapper*
    h4_wrapper: _HEADER_4 NAME _NL* variable* h5_wrapper*
    h5_wrapper: _HEADER_5 NAME _NL* variable* h6_wrapper*
    h6_wrapper: _HEADER_6 NAME _NL* variable* 

    variable: _DASH KEY value _NL*
    KEY:   /.+:/
    value: string_wrapper
         | star_list

    string_wrapper: STRING (COMMENT)*
    STRING: /[^\*].*/
    COMMENT: / *>.+/

    star_list: (_STAR element)+ _NL*
    element: STRING (COMMENT)*



    %import common.NEWLINE -> _NL
    %import common.WS
    %ignore WS

""", parser="lalr")
