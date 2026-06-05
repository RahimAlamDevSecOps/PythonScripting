import os
filename = "file1"
if os.path.exists(filename):
    print(f"{filename} already exist")
else:
    with open(filename, "w") as file:
        file.write("Hello World")
        print(f"{filename} created")

