import os
filename = "file5"
if os.path.exists(filename):
    print(f"{filename} exists. Deleting....")
    os.remove(filename)
    print(f"{filename} deleted")
else:
    print(f"{filename} does not exist")
