import os
filename = "file1"
if os.path.exists(filename):
    choice = input(f"{filename} is already exist. Do you want to overwrite it? (y/n): ")
    if choice.lower() == "y":
        print(f"Overwiting {filename}...")
        with open(filename, "w") as file:
            file.write("Hello Rahim\n")
    else:
         print(f"{filename} not overwritten")
else:
    print(f"Creating {filename}...")
    with open(filename, "w") as file:
        file.write("Hello Rahim")
