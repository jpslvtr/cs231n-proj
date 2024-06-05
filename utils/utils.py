import os
import shutil

def run_command(command):
    process = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    while True:
        output = process.stdout.readline()
        if output == b'' and process.poll() is not None:
            break
        if output:
            print(output.strip().decode())
    rc = process.poll()
    return rc

def ensure_directory_exists(path):
    if not os.path.exists(path):
        os.makedirs(path)
