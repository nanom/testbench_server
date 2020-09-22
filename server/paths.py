# --- Declear imports ---
import os

# --- List of path folders ---
ROOT = os.path.dirname(os.path.abspath(__file__))
PROPERTIES_FOLDER = os.path.join(ROOT, 'properties')
TEMPLATE_FOLDER = os.path.join(ROOT, 'template')
TEST_FOLDER = os.path.join(ROOT, 'tests')
UPLOAD_FOLDER = os.path.join(ROOT, 'upload_files')

# --- List of main path files ---
PROPERTIES_FILE = os.path.join(PROPERTIES_FOLDER, 'properties.hs')
TYPES_FUNCTION_FILE = os.path.join(PROPERTIES_FOLDER, 'function_types.hs')
