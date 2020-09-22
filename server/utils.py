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

    # Open files and create new files
    is_ok, proy_file = readFile(input_proy_file_name, "Impossible to open proy_file")
    if not is_ok:
        return 0

    is_ok, properties_file = readFile(_path.PROPERTIES_FILE, "Impossible to open properties_files")
    if not is_ok:
        return 0

    is_ok, testbench_file = writeFile(output_test_file_name, "Impossible to create testbench_file")
    if not is_ok:
        return 0

    # Get types functions
    is_ok, types_function_dic = typesfunctionToDic(_path.TYPES_FUNCTION_FILE)
    if not is_ok:
        return 0


    # Wirte head and imports
    testbench_file.write("{-# LANGUAGE ScopedTypeVariables, TemplateHaskell #-}\n")
    testbench_file.write("module Main where\n")
    testbench_file.write("import Test.QuickCheck\n\n")


    # TODO: Reformular carga de funciones para que incluya posibles funciones auxiliares
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

    is_ok, file = readFile(types_function_file, "Impossible to open types_function_file")
    if not is_ok:
        return 0, None

    for line in file:
        fun_type = line.rstrip().replace(" ","")
        if fun_type != "" and not fun_type.startswith("--"):
            dic[fun_type] = True
    file.close()

    return 1, dic


def readFile(file_path, message_by_error=""):
    try:
        file_descriptor = open(file_path, 'r')
    except IOError:
        print("Open Error!: {}.".format(message_by_error))
        return 0, None

    return 1, file_descriptor


def writeFile(file_path, message_by_error=""):
    try:
        file_descriptor = open(file_path, 'w')
    except IOError:
        print("Write Error!: {}.".format(message_by_error))
        return 0, None

    return 1, file_descriptor



if __name__ == '__main__':

    # Module Test
    print(typesfunctionToDic(_path.TYPES_FUNCTION_FILE))
