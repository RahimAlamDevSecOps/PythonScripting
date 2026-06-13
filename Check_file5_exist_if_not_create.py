import os
filename = "file7"
if os.path.exists(filename):
    print(f"{filename} is exist.")
else:
    print(f"{filename} does not exists. Creating {filename}...")
    with open(filename, "w") as file:
        print(f"{filename} created")
