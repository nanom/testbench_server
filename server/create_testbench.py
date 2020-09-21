# --- Declare Inports ---
import os
import sys
import argparse
from utils import function_types_to_dic, PROPERTIES_FOLDER, PROPERTIES_FILE, FUNCTION_TYPES_FILE


# --- Main functions ---
def create_new_testbench(function_types_dic, input_proy_file_name, output_test_file_name):

    if not os.path.isfile(input_proy_file_name):
        return sys.exit("ERROR!: Impossible to create new testbench. No Found input proyect file")

    proy_file = open(input_proy_file_name, 'r')
    properties_file = open(PROPERTIES_FILE, 'r')
    testbench_file = open(output_test_file_name,'w')

    # Wirte head and imports
    testbench_file.write("{-# LANGUAGE ScopedTypeVariables, TemplateHaskell #-}\n")
    testbench_file.write("module Main where\n")
    testbench_file.write("import Test.QuickCheck"+"\n\n")

    # Write functions to test
    testbench_file.write("-- Begin function to testing\n")
    testbench_file.write("-- ============================\n")
    for line in proy_file:
        line = line.rstrip()
        if line != "" and function_types_dic.get(line.replace(" ",""),False):
            while line and not line.startswith("--"):
                testbench_file.write(line+"\n")
                line = proy_file.readline().rstrip()
            testbench_file.write("\n\n")


    # Write property_function_name
    testbench_file.write("-- Begin property function test\n")
    testbench_file.write("-- ============================\n")
    for line in properties_file:
        line = line.rstrip()
        if line != "" and line.startswith("prop_"):
            while line and not line.startswith("--"):
                testbench_file.write(line+"\n")
                line = properties_file.readline().rstrip()
            testbench_file.write("\n\n")

    # Code to testing all property
    testbench_file.write("-- Testing all property that begin with prop_*\n")
    testbench_file.write("-- ============================\n")
    testbench_file.write("return []\n")
    testbench_file.write("main = $quickCheckAll\n")
    # testbench_file.write("main = $verboseCheckAll\n")

    proy_file.close()
    properties_file.close()
    testbench_file.close()


# --- Auxiliar functions ---
def getArguments():
    ap = argparse.ArgumentParser(description='Modo dde uso')
    ap.add_argument("-i","--input", required=True, type=str, help="Name of proy file to test")
    ap.add_argument("-o","--output", required=True, type=str, help="Name of output testbench file")
    return vars(ap.parse_args())


if __name__ == '__main__':

    args = getArguments()
    create_new_testbench(function_types_to_dic(FUNCTION_TYPES_FILE), args["input"], args["output"])
