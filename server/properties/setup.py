# --- Set to use patern modules ---
import sys
sys.path.append("../")

# --- Declare imports ---
import os
import argparse
from utils import function_types_to_dic, FUNCTION_TYPES_FILE, PROPERTIES_FILE, PROPERTIES_FOLDER

def create_properties_file():
    """
    Create properties template to fill, from function_types_dic
    """

    function_types_dic = function_types_to_dic(FUNCTION_TYPES_FILE)
    out_file = open(PROPERTIES_FILE, 'w')

    for k in function_types_dic.keys():
        prop_name = k.split("::")[0]
        prop_type = k.split("::")[1]
        out_file.write("--- property '"+prop_name+"::"+prop_type+"' ---\n")
        out_file.write("prop_"+prop_name+" :: ... -> Bool\n")
        out_file.write("prop_"+prop_name+"... = ( "+ prop_name +" ... ) == ( ... )\n")
        out_file.write("\n\n")
    out_file.close()


if __name__ == '__main__':

    create_properties_file()
    print("The file '{}' has been create succesfully in '{}'".format(PROPERTIES_FILE, PROPERTIES_FOLDER))
