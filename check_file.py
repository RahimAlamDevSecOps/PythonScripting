import os 

filename = "check_file_name_exist.py"

if os.path.exists(filename):
    print(f"{filename} exists")
else:
    print(f"{filename} does not exist")
