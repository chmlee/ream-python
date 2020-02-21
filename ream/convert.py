"""

Convert input file to output file

"""

import sys
import json
from .transformer import Ream2Json
from .parser import REAM_RULE

def convert(input_file, output_file=None):
    """
    read and convert files
    """

    # check whether input file exist
    try:
        with open(input_file, 'r') as file:
            input_raw = file.read()
    except IOError:
        print('There was an error opening the file!')
        sys.exit()

    # check file type
    convert_dict = {
        "ream": ["json"],
        "md":   ["json"],
        "json": ["md", "ream"]
    }
    input_ext = input_file.split('.')[-1]
    if input_ext not in convert_dict:
        print('Input file type not supported!')
        sys.exit()
    if output_file is not None:
        output_ext = output_file.split('.')[-1]
        if output_ext not in convert_dict[input_ext]:
            print('Output file type not supported!')
            sys.exit()
    else:
        output_ext = "json"


    if input_ext in ["ream", "md"] and output_ext in ["json"]:

        input_tree = REAM_RULE.parse(input_raw)
        output_raw = Ream2Json().transform(input_tree)

        if output_file is not None:
            with open(output_file, 'w') as file:
                json.dump(output_raw, file)

            print(json.dumps(output_raw, indent=4))

    elif input_ext in ["json"] and output_ext in ["ream", "md"]:
        with open(input_file) as json_file:
            j_raw = json.load(json_file)




    return output_raw
