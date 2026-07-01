import os
filename = "file5"
if os.path.exists(filename):
    print(f"{filename} already exist.")
else:
    print(f"{filename} does not exist. Creating {filename}")
    with open(filename, "w") as file:
        print(f"{filename} created")
