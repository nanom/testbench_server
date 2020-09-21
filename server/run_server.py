# --- Declare imports ---
import os
import subprocess
from flask import Flask, flash, request, redirect, url_for, render_template, send_from_directory
from werkzeug.utils import secure_filename
from utils import UPLOAD_FOLDER, TEST_FOLDER
from datetime import datetime
from dotenv import load_dotenv


# --- Declare constants ---
ALLOWED_EXTENSIONS = {'hs'}
CREATE_TESTBENCH_SCRIPT = 'create_testbench.py'
EXECUTE_TESTBENCH_SCRIPT = 'runhaskell'

# --- File prefix ---
PREF_TEST = 'test_'
PREF_RESULTS = 'result_'


# --- Set app configurations ---
app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['TESTS_FOLDER'] = TEST_FOLDER
app.config['MAX_CONTENT_LENGTH'] = 50 * 1024 * 1024 # Max file size allowed = 50 Mb
app.secret_key = os.urandom(24)


# --- Cargo varables de entorno ---
load_dotenv()
SERVER_PORT = os.getenv('SERVER_PORT')
SERVER_HOST = os.getenv('SERVER_HOST')



# --- Server methods ---
@app.route('/', methods=['GET', 'POST'])
def index():
    """
    Manager and deriving the form actions
    """
    messages = ""
    average = ""
    test_outputs = []

    if request.method == 'POST':
        print("request: {}".format(request.url))

        # check if the post request has the file part
        if 'file' not in request.files:
            messages = "No file part"

        else:
            file = request.files['file']

            if file.filename == '':
                messages = "No se ha seleccionado ningun archivo"
            else:
                if file and allowed_file(file.filename):
                    # Secure name verification
                    filename = secure_filename(file.filename)

                    # Rename default file_name
                    date = (datetime.now()).strftime("%H:%M:%S")
                    filename = request.remote_addr+"_"+date+"_proy.hs"

                    # Upload file
                    file.save(os.path.join(UPLOAD_FOLDER, filename))

                    # Run test and output results
                    test_outputs, average = run_test(filename)

                    # Delete file upload, test and results
                    # clean_all(filename)

                    messages = "Archivo cargado y corregido exitosamente"
                else:
                    messages = "Archivo no permitido. Solo extensiones '.hs'"

    return render_template('index.html', info={'messages':messages,'results':test_outputs, 'avg':average})

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


def run_test(filename):
    # Use os.path.relpath to hedden abspath in case of Exceptions in testing outputs
    proy_name_file = os.path.relpath(os.path.join(UPLOAD_FOLDER, filename))
    testbench_name_file = os.path.relpath(os.path.join(TEST_FOLDER, PREF_TEST+filename))
    result_name_file = os.path.relpath(os.path.join(TEST_FOLDER, PREF_RESULTS+filename))

    # Create an new testbench_name_file with incluided functions of proy file
    os.system("python {} -i {} -o {}".format(CREATE_TESTBENCH_SCRIPT, proy_name_file, testbench_name_file))

    # Execute new_test, and save results in result_name_file
    os.system("{} {} -> {} ".format(EXECUTE_TESTBENCH_SCRIPT,testbench_name_file,result_name_file))

    return get_test_results(result_name_file)

def get_test_results(result_name_file):
    # Read result_name_file with obteined tests results
    results_file = open(result_name_file,'r')
    output_results = []
    props_count = 0
    ok_cout = 0

    for line in results_file:
        if line.find("prop_") != (-1):
            props_count += 1

        if line.find("+++ OK") != (-1):
            ok_cout += 1

        line = line.rstrip().split("from")[0]
        output_results.append(line)

    results_file.close()

    average = "0" if props_count == 0 else round(ok_cout / props_count * 100.0, 1)
    return output_results, str(average)+'%'

def clean_all(filename):
    # Remove proy file upload
    path = os.path.join(UPLOAD_FOLDER, filename)
    os.system("rm {}".format(path))

    # Remove testbech file generated
    path = os.path.join(TEST_FOLDER, PREF_TEST+filename)
    os.system("rm {}".format(path))

    # Remove result file tested
    path = os.path.join(TEST_FOLDER, PREF_RESULTS+filename)
    os.system("rm {}".format(path))


# --- Main function ---
if __name__ == '__main__':
    app.run(port=SERVER_PORT, host=SERVER_HOST, debug=True, threaded=True)
