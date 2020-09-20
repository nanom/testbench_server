import os
import sys

FUNCTION_TYPE_FILE_NAME = "function_types.hs"
PROPERTY_FILE_NAME = "properties.hs"
PROY_FILE_NAME = "student_proy.hs"
TEST_FILE_NAME = "testbench.hs"

def gen_function_types_dic():
    abs_name_file = os.path.join(os.getcwd(),FUNCTION_TYPE_FILE_NAME)
    if not os.path.isfile(abs_name_file):
        return sys.exit("ERROR!: Cree en '{}', el archivo '{}' con todos los tipos de las funciones a testear en el proyecto (Una por linea).".format(os.getcwd(), FUNCTION_TYPE_FILE_NAME))

    dic = {}
    f = open(FUNCTION_TYPE_FILE_NAME,'r')
    for ftype in f:
        dic[ftype.rstrip().replace(" ","")] = True
    f.close()
    return dic.copy()


def create_property_file(function_to_test):
    property_file = open(PROPERTY_FILE_NAME, 'w')

    for k in function_to_test.keys():
        prop_name = k.split("::")[0]
        property_file.write("-- Begin "+prop_name+" property -----------\n")
        property_file.write("prop_"+prop_name+" :: ... -> Bool\n")
        property_file.write("prop_"+prop_name+"... = ( "+ prop_name +" ... ) == ...\n")
        property_file.write("\n\n")

    property_file.close()


def create_testbench_template(function_to_test):

    abs_proy_file_name = os.path.join(os.getcwd(),PROY_FILE_NAME)
    if not os.path.isfile(abs_proy_file_name):
        return sys.exit("ERROR!: Copie en '{}', el proyecto del estudiante a tester, bajo el nombre '{}'".format(os.getcwd(), PROY_FILE_NAME))

    proy_file = open(PROY_FILE_NAME, 'r')
    test_file = open(TEST_FILE_NAME,'w')

    # Wirte head and imports
    test_file.write("{-# LANGUAGE ScopedTypeVariables, TemplateHaskell #-}\n")
    test_file.write("module Main where\n")
    test_file.write("import Test.QuickCheck"+"\n\n")

    # Write functions to test
    test_file.write("-- Begin function to testing\n")
    test_file.write("-- ============================\n")
    for line in proy_file:
        line = line.rstrip()
        if function_to_test.get(line.replace(" ",""),False):
            while line != "" and not line.startswith("--"):
                test_file.write(line+"\n")
                line = proy_file.readline().rstrip()
            test_file.write("\n\n")


    # Write property_function_name
    test_file.write("-- Begin property function test\n")
    test_file.write("-- ============================\n")
    test_file.write("-- .\n")
    test_file.write("-- .\n")
    test_file.write("-- .\n")
    test_file.write("-- .\n")
    test_file.write("-- PASTE HERE THE CONTENT OF THE FILE {}\n".format(PROPERTY_FILE_NAME))
    test_file.write("-- .\n")
    test_file.write("-- .\n")
    test_file.write("-- .\n")
    test_file.write("-- .\n")
    test_file.write("-- .\n\n\n\n")


    # Code to testing all property
    test_file.write("-- Testing all property that Begin with prop_*\n")
    test_file.write("-- ============================\n")
    test_file.write("-- Execute in your terminal >$ runhaskell test_file.hs\n")
    test_file.write("return []\n")
    test_file.write("main = $quickCheckAll\n")

    proy_file.close()
    test_file.close()

if __name__ == '__main__':
    function_to_test = gen_function_types_dic()
    create_property_file(function_to_test)
    create_testbench_template(function_to_test)
    print("TODO LISTO!!:\n\tEl archivo '{}' se ha creado exitosamente en '{}'".format(TEST_FILE_NAME,os.getcwd()))
    print("\tComplete el archivo '{}' y ejecute $runhaskell {} para correr los tests".format(PROPERTY_FILE_NAME,TEST_FILE_NAME))
