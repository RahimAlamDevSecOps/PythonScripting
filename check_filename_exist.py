import os
filename = "file1"

if os.path.exists(filename):
    print(f"{filename} is exists")
else:
    print(f"{filename} does not exists")
