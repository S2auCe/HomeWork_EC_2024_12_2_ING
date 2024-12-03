import subprocess
import schedule
import time

def run_exe(file_path):
    try:
        subprocess.run({file_path})
        print(f"{file_path} executed successfully.")
    except Exception as e:
        print(f"Failed to execute {file_path}.")

file_paths = ["D:\\repos\\HomeWork_EC_2024_12_2_ING\\ExeDoc\\section1\\sec1EXE\\sec1EXE.exe","D:\\repos\\HomeWork_EC_2024_12_2_ING\\ExeDoc\\section2\\sec2EXE\\sec2EXE.exe"]

while True:
    time.sleep(5)
    for file_path in file_paths:
        run_exe(file_path)