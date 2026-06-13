import os

filename = "file1"

if os.path.exists(filename):

    choice = input(f"{filename} already exist. Do you you want to overwrite: y/n? ")
    
    if choice.lower()== "y":
        print(f"Overwriting {filename}")
        with open(filename, "w") as file:
            file.write("Hello Rahim Alam\n")
    else:
        print(f"{filename} not overwriting")
else:
    print(f"Creating {filename}")
    with open(filename, "w") as file:
        file.write("Hello Rahim Alam\n")
    
