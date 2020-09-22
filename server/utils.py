# --- Declare imports ---
import os
import sys

# --- Own ---
import paths as _path


# --- Main functions ----
def createNewTestbench(input_proy_file_name, output_test_file_name):
    """
    It generate new testbench file in 'output_test_file_name' directory. Using the
    uploaded proyect file and the properties file before generated.

    Input
        input_proy_file_name: Filename of proy to test
        output_test_file_name: Filename of testbench to create

    Output
        1: Process finaly without errors
        0: Have been an error in the process
    """

    # Open files  and create new files
    try:
        proy_file = open(input_proy_file_name, 'r')
    except IOError:
        print("ERROR!: Impossible to open proy_file.")
        return 0

    try:
        properties_file = open(_path.PROPERTIES_FILE, 'r')
    except IOError:
        print("ERROR!: Impossible to open properties_files.")
        return 0

    try:
        testbench_file = open(output_test_file_name,'w')
    except IOError:
        print("ERROR!: Impossible to create testbecnh_file.")
        return 0


    # Get types functions
    res, types_function_dic = typesfunctionToDic(_path.TYPES_FUNCTION_FILE)
    if not res:
        return 0


    # Wirte head and imports
    testbench_file.write("{-# LANGUAGE ScopedTypeVariables, TemplateHaskell #-}\n")
    testbench_file.write("module Main where\n")
    testbench_file.write("import Test.QuickCheck\n\n")

    # Write functions to test
    testbench_file.write("-- Begin function to testing\n")
    testbench_file.write("-- ============================\n")
    for line in proy_file:
        line = line.rstrip()
        if line != "" and types_function_dic.get(line.replace(" ",""),False):
            while line != "" and not line.startswith("--"):
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
    return 1


# --- List of auxiliar functions ----
def typesfunctionToDic(types_function_file):
    """
    It Convert file of types function to compact dictionary.
    It Clean white spaces to improvement matching.

    Input
        types_function_file: Filename of types_function_file.

    Output
        1, dic: Return dictionary of types functions,
        0, {} : Have been an error in the process
    """

    dic = {}

    try:
        file = open(types_function_file,'r')
    except IOError:
        print("ERROR!: Impossible to open types_function_file.")
        return 0, dic

    for line in file:
        fun_type = line.rstrip().replace(" ","")
        if fun_type != "" and not fun_type.startswith("--"):
            dic[fun_type] = True
    file.close()

    return 1, dic


if __name__ == '__main__':

    # Module Test
    print(typesfunctionToDic(_path.TYPES_FUNCTION_FILE))
