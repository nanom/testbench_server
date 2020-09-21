import os
import sys

# --- List of path folders ---
# ROOT = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(__file__)
PROPERTIES_FOLDER = os.path.join(ROOT, 'properties')
TEMPLATE_FOLDER = os.path.join(ROOT, 'template')
TEST_FOLDER = os.path.join(ROOT, 'tests')
UPLOAD_FOLDER = os.path.join(ROOT, 'upload_files')

# --- List of main path files ---
PROPERTIES_FILE = os.path.join(PROPERTIES_FOLDER, 'properties.hs')
FUNCTION_TYPES_FILE = os.path.join(PROPERTIES_FOLDER, 'function_types.hs')


# --- List of auxiliar functions ----
def function_types_to_dic(function_types_file):
    """
    Convert file of function types to compact dic.
    Clean with spaces to matching improvment.
    """

    if not os.path.isfile(function_types_file):
        return sys.exit("ERROR!: No se puede abrir el archivo {}!".format(function_types_file))

    dic = {}
    file = open(function_types_file,'r')
    for line in file:
        fun_type = line.rstrip().replace(" ","")
        if fun_type != "" and not fun_type.startswith("--"):
            dic[fun_type] = True
    file.close()
    return dic.copy()

if __name__ == '__main__':

    # Test
    print(function_types_to_dic(FUNCTION_TYPES_FILE))
