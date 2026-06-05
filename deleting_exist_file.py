import os
filename = "file1"
if os.path.exists(filename):
    print(f"{filename} is exist. Deleting {filename}")

    os.remove(filename)
    print(f"{filename} deleted successfully")

else:
    print(f"{filename} does not exists")
