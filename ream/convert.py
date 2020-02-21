"""

Convert input file to output file

"""

import json
from .transformer import Ream2Json
from .parser import REAM_RULE

def convert(input_file, output_file):
    """
    read, convert and dump files
    """
    # read input file
    with open(input_file, 'r') as file:
        input_raw = file.read()

    input_tree = REAM_RULE.parse(input_raw)

    output_raw = Ream2Json().transform(input_tree)

    with open(output_file, 'w') as file:
        json.dump(output_raw, file)

    print(json.dumps(output_raw, indent=4))

    return output_raw
