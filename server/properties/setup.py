# --- Set to use patern modules ---
import sys
sys.path.append("..")

# --- Declare imports ---
import os
import argparse


# --- Own ---
import paths as _path
import utils as _util


# --- Main functions ---
def createPropertiesFile():
    """
    Create properties template to fill, from types_function_dic

    Output
        1: Process finaly without errors
        0: Have been an error in the process
    """

    # Check if file exit
    if os.path.isfile(_path.PROPERTIES_FILE):
        opc = input("The file already exists. Do you it overwrite? (y|n): ")
        if opc.lower() == "n":
            return 1


    # Open properties file
    try:
        out_file = open(_path.PROPERTIES_FILE, 'w')
    except IOError:
        print("ERROR!: Impossible to create properties_file.")
        return 0

    res, types_function_dic = _util.typesfunctionToDic(_path.TYPES_FUNCTION_FILE)
    if not res:
        return 0

    for k in types_function_dic.keys():
        prop_name = k.split("::")[0]
        prop_type = k.split("::")[1]
        out_file.write("--- property '"+prop_name+"::"+prop_type+"' ---\n")
        out_file.write("prop_"+prop_name+" :: ... -> Bool\n")
        out_file.write("prop_"+prop_name+" ... = ( "+ prop_name +" ... ) == ( ... )\n")
        out_file.write("\n\n")
    out_file.close()

    return 1


if __name__ == '__main__':

    # Tests
    result = "The file '{}' has been create succesfully in '{}'".format(_path.PROPERTIES_FILE, _path.PROPERTIES_FOLDER)
    result if not createPropertiesFile() else None
